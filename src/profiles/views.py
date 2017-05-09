from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.core import serializers
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.contrib.auth.models import AnonymousUser
from django.contrib.auth import authenticate, login
from django.http import HttpRequest
from sqlalchemy import create_engine
from database.forms import CommentForm, DocumentForm, ActionForm,RequestForm
from profiles.models import profile
from database.models import ScComments, Document, ScAnsActionNew,ScActionNotif, ScRequests, ScRequestsCategories,ScAnsCategories
from database.views import getRequests,sentRequests,getParentRequestsAll,getUserCategories,getActions,getUsers,setUserTag,getTaggedUsers
from database.views import getRequestByID,getCommentsByID,getNotifications,getUserID,setUserNotifs,updateRequestDoneDB,getUserData,ScAnsActionNotif
from database.views import getAllCategoryRequests,getUserCategoriesForRequest,getSearchRequests,getUserStatus,updateRequestLockedDB,getUnreadRequests
from profiles.ipLogin import *
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from profiles.setNotifRead import *
from profiles.sendNotification import *
from django.utils import timezone
from django.shortcuts import (render_to_response)
from django.template import RequestContext
import logging
from itertools import chain
import datetime
import unicodedata
import pdb
import ipaddress
import re
import datetime
import random
import os
import time
import json
from itertools import chain

# Create your views here.
# Get user IP address for login process
def home(request):
	# First check IP address
	if request.user == AnonymousUser():
		ip_address  = get_ip_address(request)
		user_logged = login_ip_address(request,ip_address,request.user)

	if request.user.is_authenticated:
		parentUsername = getParentUsername(request)
		#notifications = getNotifications(request)
		#requests = getRequests(request)
		requests = getUnreadRequests(request)
		user_categories_names = getUserCategories(request,parentUsername)
		chart = []

		if requests:
			openR = requests.filter(status="open").count()
			closedR = requests.filter(status="closed").count()
			lockedR = requests.filter(status__contains="lock").count()
			if openR>0 or closedR>0 or lockedR>0:
				chart=[openR,closedR,lockedR]
			else:
				deletedR = requests.filter(status="deleted").count()
				chart=[deletedR]
		#allCategoryRequests = getAllCategoryRequests(request,user_categories_requests)

		#requests = list(chain(sentRequestResult, tagRequests, parentRequestResult))
		data = {'requests':requests,'catNames':user_categories_names,'chart':chart,
		        'activeCategory':'taggedRequests'}
		template = "home.html"
		#pdb.set_trace()
		return render(request,template,data)
	else:
		return HttpResponseRedirect('accounts/login')
	
    # user_cat_name ->    <QuerySet [(17, u'AGIS - Debitor'), (15, u'Test')]>
    # user_cat_request -> <QuerySet [(15, 1056), (15, 1149), (15, 1065), (15, 1132)]

	#jsonCatRequests = serializers.serialize('json', list(user_categories_requests))
	#parsedCatRequests = json.loads(jsonCatRequests)

def getParentUsername(request):
	parentUsername = ScAns.objects.filter(username=request.user.username).values_list("parent_username",flat=True)[0]
	return parentUsername

def getSentRequests(request):
	parentUsername = getParentUsername(request)
	requests = sentRequests(request)
	user_categories_names = getUserCategories(request,parentUsername)
	chart = []

	if requests is not None:
		openR = requests.filter(status="open").count()
		closedR = requests.filter(status="closed").count()
		lockedR = requests.filter(status__contains="lock").count()
		if openR>0 or closedR>0 or lockedR>0:
			chart=[openR,closedR,lockedR]
		else:
			deletedR = requests.filter(status="deleted").count()
			chart=[deletedR]

	data = {'requests':requests,'catNames':user_categories_names,'chart':chart,'activeCategory':'sentRequests'}
	template = "home.html"
	return render(request,template,data)

def otherRequests(request):
	parentUsername = getParentUsername(request)
	req_ids = ScRequestsCategories.objects.filter(cat_id=3).values_list('req_id',flat=True)
	requests = ScRequests.objects.filter(id__in=req_ids)
	user_categories_names = getUserCategories(request,parentUsername)
	chart = []
	
	if requests is not None:
		openR = requests.filter(status="open").count()
		closedR = requests.filter(status="closed").count()
		lockedR = requests.filter(status__contains="lock").count()
		if openR>0 or closedR>0 or lockedR>0:
			chart=[openR,closedR,lockedR]
		else:
			deletedR = requests.filter(status="deleted").count()
			chart=[deletedR]

	data = {'requests':requests,'catNames':user_categories_names,'chart':chart,'activeCategory':'otherRequests'}
	template = "home.html"
	return render(request,template,data)

def getParentRequests(request):
	parentUsername = getParentUsername(request)
	requests = getParentRequestsAll(request)
	user_categories_names = getUserCategories(request,parentUsername)
	chart = []
	
	if requests is not None:
		openR = requests.filter(status="open").count()
		closedR = requests.filter(status="closed").count()
		lockedR = requests.filter(status__contains="lock").count()
		if openR>0 or closedR>0 or lockedR>0:
			chart=[openR,closedR,lockedR]
		else:
			deletedR = requests.filter(status="deleted").count()
			chart=[deletedR]

	data = {'requests':requests,'catNames':user_categories_names,'chart':chart,'activeCategory':'ParentRequests'}
	template = "home.html"
	return render(request,template,data)

def getCatRequests(request):
	parentUsername = getParentUsername(request)
	cat_id = request.POST.get("catID", "")

	requestIDs = ScRequestsCategories.objects.filter(cat_id=cat_id).values_list('req_id',flat=True)
	requests = ScRequests.objects.filter(id__in=requestIDs)
	chart = []

	if requests:
		openR = requests.filter(status="open").count()
		closedR = requests.filter(status="closed").count()
		lockedR = requests.filter(status__contains="lock").count()
		if openR>0 or closedR>0 or lockedR>0:
			chart=[openR,closedR,lockedR]
		else:
			deletedR = requests.filter(status="deleted").count()
			chart=[deletedR]

	user_categories_names = getUserCategories(request,parentUsername)
	data = {'requests':requests,'catNames':user_categories_names,'chart':chart,'activeCategory':cat_id}
	template = "home.html"
	return render(request,template,data)

def setUserStatus(userStatusList):
	if [y for y in userStatusList if "aa" in y]:
		userStatus = "aa"
	else:
		if [y for y in userStatusList if "ak" in y]:
			userStatus = "ak"
		else:
			if [y for y in userStatusList if "ar" in y]:
				userStatus = "ar"
			else:
				userStatus = "ak"
	return userStatus

def about(request):
	req_id = request.POST.get("request_id", "")
	notif_id = request.POST.get("notif_id", "")
	userStatus=""
	userStatusList=[]
	#getNotifications(request)
	
	if notif_id:
		setNotifRead(request, notif_id)
	
	'''
	notif_pk_id = Notification.objects.filter(target_object_id=req_id).filter(unread=True).filter(recipient=request.user).values_list('pk',flat=True)
	if(notif_pk_id):
		setNotifRead(request, notif_pk_id)
		getNotifications(request)
		'''

	singleRequest = getRequestByID(request,req_id)

	userStatusList = getUserStatus(request,req_id)
	userStatus = setUserStatus(userStatusList)

	comments = getCommentsByID(request,req_id)
	actions = getActions(request,req_id)
	users = getUsers(request)
	tags = getTaggedUsers(request,req_id)

	data = {"tags":tags,'users':users, 'singleRequest':singleRequest,'comments':comments,'actions':actions,'userStatus':userStatus}
	template = "about.html"
	return render(request,template,data)

def addComment(request):
	request_id = request.POST.get("request_id", "")
	message = request.POST.get("message", "")
	i = datetime.datetime.now().replace(microsecond=0)

	form = CommentForm(request.POST, request.FILES)
	if form.is_valid():
		obj = ScComments()
		fileObj = Document()

		obj.req_id = int(request_id)
		obj.ans_id = request.user.username
		obj.ins_date = "%s" % i
		obj.comment_text = message

		if request.FILES:
			myFile = request.FILES['fileupload']
			myFileList = myFile.name.split('.')
			obj.file_path = 'comment/{0}/{1}/{2}{3}{4}.{5}'.format(request_id, request.user, i.hour, i.minute,i.second,
			                                                    myFile.name.split(".")[-1])

			fileObj.user = request.user
			fileObj.request_id = request_id
			fileObj.path = obj.file_path 
			fileObj.document = myFile
			fileObj.save()

		obj.save()
		actionObj = ScAnsActionNew()
		actionObj.user_id = getUserID(request)
		actionObj.action_id = 6
		actionObj.req_id = request_id
		actionObj.a_date = i.strftime("%Y-%m-%d")
		actionObj.save()

		
	setUserNotifs(request,request_id,actionObj.id)
	#getNotifications(request)

	userStatusList = getUserStatus(request,request_id)
	userStatus = setUserStatus(userStatusList)

	actions = getActions(request,request_id)
	singleRequest = getRequestByID(request,request_id)
	comments = getCommentsByID(request,request_id)
	users = getUsers(request)
	tags = getTaggedUsers(request,request_id)

	data = {'tags':tags,'users':users,'singleRequest':singleRequest,'comments':comments,'actions':actions,'userStatus':userStatus}

	template = "about.html"
	return render(request,template,data)

def getID():
	reqIDmax = ScRequests.objects.last()
	reqID = int(reqIDmax.id) + 1
	return reqID

def addRequest(request):
	title = request.POST.get("title", "")
	message = request.POST.get("message", "")
	category = request.POST.get("category", "")
	i = datetime.datetime.now().replace(microsecond=0)

	if title and message and category:
		requestObject = ScRequests()
		requestObject.id = getID()
		requestObject.title = title
		requestObject.description = message
		requestObject.status = "open"
		requestObject.sender = request.user.username
		requestObject.ins_date = i.now().replace(microsecond=0)

		if request.FILES:
			myFile = request.FILES['myFile']
			requestObject.file_path = 'request/{0}/{1}/{2}{3}{4}.{5}'.format(requestObject.id,request.user, i.hour, 
				                                                          i.minute,i.second,myFile.name.split(".")[-1])

			fileObj = Document()
			fileObj.user = request.user
			fileObj.request_id = requestObject.id
			fileObj.path = requestObject.file_path
			fileObj.document = myFile
			fileObj.save()

		requestObject.save()

		requestCatObject = ScRequestsCategories()
		requestCatObject.req_id = requestObject.id
		requestCatObject.cat_id = category
		requestCatObject.save()


		catUsers = ScAnsCategories.objects.filter(cat_id=category).values_list('ans_username',flat=True).distinct()
		for catUser in catUsers:
			userID = User.objects.filter(username=catUser).values_list('id',flat=True)
			if userID:
				actionObjNotif = Notification()
				actionObjNotif.level = "info"
				actionObjNotif.unread = 1
				actionObjNotif.actor_object_id = request.user.id
				actionObjNotif.target_object_id = requestObject.id
				actionObjNotif.verb = "sorgu yaratdi"
				actionObjNotif.description = "sorgu yaratdi"
				actionObjNotif.timestamp = timezone.now()
				actionObjNotif.public = 1
				actionObjNotif.actor_content_type_id = 3
				actionObjNotif.recipient_id = userID[0]
				actionObjNotif.deleted = 0
				actionObjNotif.emailed = 0
				actionObjNotif.data = ""
				actionObjNotif.save()

			ansActionNotifObject = ScAnsActionNotif()
			actIDmax = ScAnsActionNotif.objects.last()
			ansActionNotifObject.id = int(actIDmax.id) + 1
			ansActionNotifObject.action_id = 2
			ansActionNotifObject.req_id = requestObject.id
			ansActionNotifObject.who_see = catUser
			ansActionNotifObject.notif = "unread"
			ansActionNotifObject.save()


		'''
		actionNewObject = ScAnsActionNew()
		actionNewObject.user_id = getUserID(request)
		actionNewObject.action_id = 2
		actionNewObject.req_id = requestObject.id
		actionNewObject.a_date = i.strftime("%Y-%m-%d")
		actionNewObject.save()
		'''
		#pdb.set_trace()

		data = {'req_id':requestObject.id}
		template = "requestSentSuccess.html"
		return render(request,template,data)
	else:
		user_categories_names = getUserCategoriesForRequest(request)
		context={'catNames':user_categories_names,'message':"Ugurlu olmadi: Basliq,mesaj ve kateqoriya secmek mutleqdir."}
		template = "request.html"
		return render(request,template,context)

def updateRequestDone(request):
	req_id = request.POST.get("request_id", "")
	username = request.user.username
	updateRequestDoneDB(username, req_id)
	users = getUsers(request)

	singleRequest = getRequestByID(request,req_id)
	actions = getActions(request,req_id)
	comments = getCommentsByID(request,req_id)
	tags = getTaggedUsers(request,req_id)

	closerID = ScAns.objects.filter(username=username).values_list('id',flat=True)
	requestCreaterUsername = ScRequests.objects.filter(id=req_id).values_list('sender',flat=True)
	requestCreaterID = ScAns.objects.filter(username=requestCreaterUsername).values_list('id',flat=True)
	commentUsersID = ScAnsActionNew.objects.filter(req_id=req_id).exclude(user_id=closerID).exclude(user_id=requestCreaterID[0]).values_list('user_id',flat=True).distinct()

	for commentUserID in commentUsersID:
		#userID = User.objects.filter(username=catUser).values_list('id',flat=True)
		userID = profile.objects.filter(id=commentUserID).values_list("user_id",flat=True)
		if userID:
			actionObjNotif = Notification()
			actionObjNotif.level = "info"
			actionObjNotif.unread = 1
			actionObjNotif.actor_object_id = request.user.id
			actionObjNotif.target_object_id = req_id
			actionObjNotif.verb = "sorgunu bagladi"
			actionObjNotif.description = "sorgunu bagladi"
			actionObjNotif.timestamp = timezone.now()
			actionObjNotif.public = 1
			actionObjNotif.actor_content_type_id = 3
			actionObjNotif.recipient_id = userID[0]
			actionObjNotif.deleted = 0
			actionObjNotif.emailed = 0
			actionObjNotif.data = ""
			actionObjNotif.save()

	userStatusList = getUserStatus(request,req_id)
	userStatus = setUserStatus(userStatusList)

	data = {'tags':tags,'users':users,'singleRequest':singleRequest,'comments':comments,'actions':actions,'userStatus':userStatus}
	
	template = "about.html"
	return render(request,template,data)

def updateRequestLocked(request):
	req_id = request.POST.get("request_id", "")
	username = request.user.username
	updateRequestLockedDB(username, req_id)
	users = getUsers(request)

	singleRequest = getRequestByID(request,req_id)
	actions = getActions(request,req_id)
	comments = getCommentsByID(request,req_id)
	tags = getTaggedUsers(request,req_id)

	lockerID = ScAns.objects.filter(username=username).values_list('id',flat=True)
	requestCreaterUsername = ScRequests.objects.filter(id=req_id).values_list('sender',flat=True)
	requestCreaterID = ScAns.objects.filter(username=requestCreaterUsername).values_list('id',flat=True)
	commentUsersID = ScAnsActionNew.objects.filter(req_id=req_id).exclude(user_id=lockerID).exclude(user_id=requestCreaterID[0]).values_list('user_id',flat=True).distinct()

	for commentUserID in commentUsersID:
		#userID = User.objects.filter(username=catUser).values_list('id',flat=True)
		userID = profile.objects.filter(id=commentUserID).values_list("user_id",flat=True)
		if userID:
			actionObjNotif = Notification()
			actionObjNotif.level = "info"
			actionObjNotif.unread = 1
			actionObjNotif.actor_object_id = request.user.id
			actionObjNotif.target_object_id = req_id
			actionObjNotif.verb = "sorgunu lock etdi"
			actionObjNotif.description = "sorgunu lock etdi"
			actionObjNotif.timestamp = timezone.now()
			actionObjNotif.public = 1
			actionObjNotif.actor_content_type_id = 3
			actionObjNotif.recipient_id = userID[0]
			actionObjNotif.deleted = 0
			actionObjNotif.emailed = 0
			actionObjNotif.data = ""
			actionObjNotif.save()

	if requestCreaterID[0]:
		actionObjNotif = Notification()
		actionObjNotif.level = "info"
		actionObjNotif.unread = 1
		actionObjNotif.actor_object_id = request.user.id
		actionObjNotif.target_object_id = req_id
		actionObjNotif.verb = "sorgunu lock etdi"
		actionObjNotif.description = "sorgunu lock etdi"
		actionObjNotif.timestamp = timezone.now()
		actionObjNotif.public = 1
		actionObjNotif.actor_content_type_id = 3
		actionObjNotif.recipient_id = profile.objects.filter(id=requestCreaterID).values_list("user_id",flat=True)[0]
		actionObjNotif.deleted = 0
		actionObjNotif.emailed = 0
		actionObjNotif.data = ""
		actionObjNotif.save()

	userStatusList = getUserStatus(request,req_id)
	userStatus = setUserStatus(userStatusList)

	data = {'tags':tags,'users':users,'singleRequest':singleRequest,'comments':comments,'actions':actions,'userStatus':userStatus}
	
	template = "about.html"
	return render(request,template,data)

def tagUser(request):
	userList = request.POST.getlist('userList')
	request_id = request.POST.get("request_id", "")

	if userList:
		isPreviousTag = setUserTag(request,request_id,userList)
		users = getUsers(request)
		singleRequest = getRequestByID(request,request_id)
		actions = getActions(request,request_id)
		comments = getCommentsByID(request,request_id)
		tags = getTaggedUsers(request,request_id)

		userStatusList = getUserStatus(request,request_id)
		userStatus = setUserStatus(userStatusList)

		template = "about.html"
		context = {'tags':tags,'users':users,'singleRequest':singleRequest,'isPreviousTag':isPreviousTag,
		           'comments':comments,'actions':actions,'userStatus':userStatus}
	else:
		template = "notSucceed.html"
		error = "Requeste uygun hec bir istifadeci secmediniz." 
		context = {"error":error}

	return render(request,template,context)

def updateUserProfile(request):
	new_ip = request.POST.get("ip", "")
	email = request.POST.get("email", "")
	internal_tel_num = request.POST.get("internal_tel_num", "")
	mob_tel_num = request.POST.get("mob_tel_num", "")
	message = ""
	messageType = ""

	if new_ip:
		pat = re.compile("^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$")
		test = pat.match(new_ip)
		if test:
			request.user.profile.ip = new_ip
			ScAns.objects.filter(username=request.user.username).update(ip=new_ip)
		else:
			message += "- IP address duzgun daxil edilmeyib\n"
			messageType = "danger"

	if email:
		from django.core.exceptions import ValidationError
		from django.core.validators import validate_email
		try:
			validate_email(email)
		except ValidationError as e:
			message += "- Email duzgun formada qeyd edilmeyib\n"
			messageType = "danger"
		else:
			ScAns.objects.filter(username=request.user.username).update(email=email)

	if internal_tel_num:
		if internal_tel_num.isdigit():
			request.user.profile.internal_tel_num = internal_tel_num
			ScAns.objects.filter(username=request.user.username).update(internal_tel_num=internal_tel_num)
		else:
			message += "- Daxili nomre duzgun daxil edilmeyib\n"
			messageType = "danger"

	if mob_tel_num:
		if internal_tel_num.isdigit():
			request.user.profile.mob_tel_num = mob_tel_num
			ScAns.objects.filter(username=request.user.username).update(mob_tel_num=mob_tel_num)
		else:
			message += "- Mobil nomre duzgun daxil edilmeyib\n"
			messageType = "danger"

	if not message:
		message = "Qeyd edildi"
		messageType = "success"

	request.user.profile.save()
	profile = getUserData(request)
	context = {'profile': profile,'message':message,'messageType':messageType}
	template = 'profile.html'
	return render(request,template,context)

def search(request):
	searchKey = request.POST.get("key", "")
	if not searchKey:
		searchKey = request.GET.get("key", "")

	searchRequestsInitial = getSearchRequests(request,searchKey)
	searchCount = searchRequestsInitial.count()

	page = request.GET.get('page', 1)
	paginator = Paginator(searchRequestsInitial, 10)

	try:
		searchRequests = paginator.page(page)
	except PageNotAnInteger:
		searchRequests = paginator.page(1)
	except EmptyPage:
		searchRequests = paginator.page(paginator.num_pages)

	context = {'searchRequests':searchRequests,'searchCount':searchCount,'searchKey':searchKey}
	template = "searchResult.html"
	return render(request,template,context)

def bootTable(request):
	context = locals()
	template = "bootTable.html"
	return render(request,template,context)

def dataTable(request):
	context = locals()
	template = "dataTable.html"
	return render(request,template,context)

@login_required
def userProfile(request):
	profile = getUserData(request)
	context = {'profile': profile}
	template = 'profile.html'
	return render(request,template,context)

@login_required
def makeRequest(request):
	#user = request.user
	user_categories_names = getUserCategoriesForRequest(request)
	context = {'catNames':user_categories_names}
	template = 'request.html'
	return render(request,template,context)

def page_not_found(request):
	response = render_to_response('404.html',context_instance=RequestContext(request))
	response.status_code = 404
	return response
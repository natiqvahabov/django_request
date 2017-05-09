from database.models import ScComments,ScRequests,ScRequestTags,ScAnsParent,ScAnsCategories,ScCategories,ScAns
from database.models import ScRequestsCategories,ScAnsAction,ScActionNotif,ScAnsActionNew,ScAnsActionNotif
from django.shortcuts import render
from django.contrib.auth.models import User
from notifications.models import Notification
from django.db.models import Q
from profiles.models import profile
from django.core import serializers
from itertools import chain
import datetime
from django.utils import timezone
import json


# Create your views here.
def getUserData(request):
	profile = ScAns.objects.get(username=request.user.username)
	return profile

def getUsers(request):
	users = ScAns.objects.select_related('user')
	return users

def getRequests(request):
	username = request.user.username
	requests_ids = ScRequestTags.objects.filter(tagged_user=username).values_list('req_id', flat=True)
	#user_categories_ids = ScAnsCategories.objects.filter(ans_username=username).values_list('cat_id', flat=True)

	if requests_ids:	
		requests = ScRequests.objects.filter(id__in=requests_ids)
		return requests
	else:
		print("Requests object is null!")

def getUnreadRequests(request):
	#newRequestIDs = Notification.objects.filter(recipient=request.user).filter(unread=True).filter(verb="sorgu yaratdi").values_list("target_object_id",flat=True)
	newRequestIDs = ScAnsActionNotif.objects.filter(who_see=request.user.username).filter(notif='unread').filter(action_id='2').values_list('req_id',flat=True)
	if newRequestIDs:
		requests = ScRequests.objects.filter(id__in=newRequestIDs).filter(status='open')
		return requests
	else:
		print("Requests object is null!")

def getUserStatus(request,request_id):
	username = request.user.username
	category = ScRequestsCategories.objects.filter(req_id=request_id).values_list('cat_id',flat=True)[0]
	status = ScAnsCategories.objects.filter(cat_id=category).filter(ans_username=username).values_list('utype',flat=True)
	return status

def getRequestByID(request,req_id):
	singleRequest = ScRequests.objects.get(id__exact=req_id)

	if singleRequest:
		return singleRequest
	else:
		print("RequestsByID object is null!")
		return request


def getParentRequestsAll(request):
	username = request.user.username
	parentUser = ScAnsParent.objects.filter(child_name=username).values_list('parent_name', flat=True)

	if parentUser is not None:
		requests_ids = ScRequestTags.objects.filter(tagged_user=parentUser).values_list('req_id', flat=True)
		if requests_ids is not None:
			requests = ScRequests.objects.filter(id__in=requests_ids)
			return requests
		else:
			print("Parent Request IDs object is null!")
	else:
		print("Parent Requests object is null!")


def sentRequests(request):
	username = request.user.username
	requests = ScRequests.objects.filter(sender=username)

	if requests:
		return requests
	else:
		print("SentRequests object is null!")
		return requests


def getCommentsByID(request,request_id):
	comments = ScComments.objects.filter(req_id__exact=request_id).order_by('ins_date')

	if comments:
		return comments
	else:
		print("Comments object is null!")


def setComment(request,req_id,messageSuccess):
	result = ScComments.objects.filter(req_id__exact=request_id).order_by('ins_date')

	if result is True:
		return comments
	else:
		print("Comments object is null!")
		

def getUserCategories(request,parentUsername):
	user_categories_ids = ScAnsCategories.objects.filter(ans_username=parentUsername).values_list('cat_id', flat=True)

	if user_categories_ids:
		user_categories_names = ScCategories.objects.filter(id__in=user_categories_ids).values_list('id','name')
		#user_categories_requests = ScRequestsCategories.objects.filter(cat_id__in=user_categories_ids)
		#user_categories_requests_ids = ScRequestsCategories.objects.filter(cat_id__in=user_categories_ids).values_list('req_id',flat=True)
		#allCatRequests = ScRequests.objects.filter(id__in=user_categories_requests_ids)

		if user_categories_names:
			return user_categories_names
		else:
			print("User categories names object is null!")
			return user_categories_names	
	else:
		print("User categories ids object is null!")
		return user_categories_ids


def getUserCategoriesForRequest(request):
	username = request.user.username
	user_categories_ids = ScAnsCategories.objects.filter(ans_username=username).filter(utype="ar").values_list('cat_id', flat=True)
	if user_categories_ids:
		user_categories_names = ScCategories.objects.filter(id__in=user_categories_ids).values_list('id','name')
		if user_categories_names:
			return user_categories_names
		else:
			print("User categories names object is null!")
			return user_categories_names	
	else:
		print("User categories ids object is null!")
		return user_categories_ids


def getAllCategoryRequests(request,categories):
	categoryRequests=[]
	for category in categories:
		categoryRequests += ScRequests.objects.filter(id = category.req_id).filter(Q(status="open") | Q(status__contains="lock"))


def getNotifications(request):
	username = request.user.username
	#notifications = Notification.objects.filter(recipient=request.user).filter(unread=1)
	notifications = request.user.notifications.unread()
	
	if notifications:
		return notifications
	else:
		print "Notifications object is null"

	'''
	if notifications:
		data = {'notifications':notifications}
		request.session.modified = True
		jsonCatRequests = serializers.serialize('json', list(notifications))
		parsedCatRequests = json.loads(jsonCatRequests)
		request.session['notifications'] = list(parsedCatRequests)
	else:
		print("Notifications object is null!")
		return request
	'''


def updateRequestDoneDB(username,req_id):
	request = ScRequests.objects.filter(id=req_id).update(status="closed")
	userID = ScAns.objects.filter(username=username).values_list('id',flat=True)[0]
	
	if request:
		actionObject = ScAnsActionNew()
		actionObject.user_id = userID
		actionObject.action_id = 3
		actionObject.req_id = req_id 
		actionObject.a_date = datetime.datetime.now().strftime("%Y-%m-%d")
		actionObject.save()

	return

def updateRequestLockedDB(username,req_id):
	request = ScRequests.objects.filter(id=req_id).update(status="locked")
	userID = ScAns.objects.filter(username=username).values_list('id',flat=True)[0]
	
	if request:
		actionObject = ScAnsActionNew()
		actionObject.user_id = userID
		actionObject.action_id = 5
		actionObject.req_id = req_id
		actionObject.a_date = datetime.datetime.now().strftime("%Y-%m-%d")
		actionObject.save()

	return

def getActions(request,req_id):
	#username = request.user.username
	#userID = ScAns.objects.filter(username=username).values_list('id',flat=True)[0]
	actions_old = ScAnsAction.objects.filter(req_id=req_id).filter(action_id__in=[3,5])
	actions_new = ScAnsActionNew.objects.filter(req_id=req_id).filter(action_id__in=[3,5])
	actions = list(chain(actions_old, actions_new))

	return actions


def setUserTag(request,request_id,userList):
	username = request.user.username
	isPreviousTag = []

	for userID in userList:
		tagged_user_name = ScAns.objects.filter(id=int(userID)).values_list("username",flat=True)[0]
		condition = ScRequestTags.objects.filter(req_id=request_id).filter(tagged_user=tagged_user_name)
		if condition:
			isPreviousTag.append("- " + str(tagged_user_name) + " bu requeste daha once elave olunub")
		else:
			tagObj = ScRequestTags()
			lastTag = ScRequestTags.objects.last()
			tagObj.id = int(lastTag.id) + 1
			tagObj.req_id = request_id
			tagObj.tagged_date = datetime.datetime.now().strftime("%Y-%m-%d")
			tagObj.tagged_user = tagged_user_name
			tagObj.view_status = "unread"
			tagObj.who_tagged = username
			tagObj.save()

	return isPreviousTag

def getSearchRequests(request,searchKey):
	username = request.user.username
	user_categories_ids = ScAnsCategories.objects.filter(ans_username=username).values_list('cat_id', flat=True).distinct()
	user_categories_requests_ids = ScRequestsCategories.objects.filter(cat_id__in=user_categories_ids).values_list('req_id',flat=True)
	searchRequestsInitial = ScRequests.objects.filter(description__contains=searchKey).filter(id__in = user_categories_requests_ids).order_by('-ins_date')
	return searchRequestsInitial


def getUserID(request):
	username = request.user.username
	user_id = ScAns.objects.filter(username=username).values_list('id',flat=True)

	if user_id:
		return user_id[0]
	else:
		print("ID object is null!")


def getTaggedUsers(request,request_id):
	tags = ScRequestTags.objects.filter(req_id=request_id).values_list("tagged_user","who_tagged")
	if tags:
		return tags
	else:
		print "Tags object is null"


def setUserNotifs(request,request_id,actionObj_id):
	username = request.user.username
	object_id_list = ScAns.objects.filter(username=username).values_list('id',flat=True)
	profile_id = request.user.id
	requestCreaterUsername = ScRequests.objects.filter(id=request_id).values_list('sender',flat=True)
	requestCreaterID = ScAns.objects.filter(username=requestCreaterUsername).values_list('id',flat=True)
	requestProfileID = User.objects.filter(username=requestCreaterUsername[0]).values_list('id',flat=True)
	actionUsers = ScAnsActionNew.objects.filter(req_id=request_id).exclude(user_id=object_id_list).exclude(user_id=requestCreaterID[0]).values_list('user_id',flat=True).distinct()

    # send notification to users who has commented on that request
	for actionUser in actionUsers:
		user_i = profile.objects.filter(id=actionUser).values_list("user_id",flat=True)
		if user_i:
			actionObj = ScActionNotif()
			actionObj.action_id = actionObj_id
			actionObj.user_id = actionUser
			actionObj.notif = "unread"
			actionObj.save()

			actionObjNotif = Notification()
			actionObjNotif.level = "info"
			actionObjNotif.unread = 1
			actionObjNotif.actor_object_id = request.user.id
			actionObjNotif.target_object_id = request_id
			actionObjNotif.verb = "serh bildirdi"
			actionObjNotif.description = "commented on your request"
			actionObjNotif.timestamp = timezone.now()
			actionObjNotif.public = 1
			actionObjNotif.actor_content_type_id = 3
			actionObjNotif.recipient_id = user_i[0]
			actionObjNotif.deleted = 0
			actionObjNotif.emailed = 0
			actionObjNotif.data = ""
			actionObjNotif.save()

	# send notification to the creator of the request
	actionObj = ScActionNotif()
	actionObj.action_id = actionObj_id
	actionObj.user_id = requestCreaterID[0]
	actionObj.notif = "unread"
	actionObj.save()

	# requestCreaterID ---- 22
	if username != requestCreaterUsername[0]:
		actionObjNotif = Notification()
		actionObjNotif.level = "info"
		actionObjNotif.unread = 1
		actionObjNotif.actor_object_id = request.user.id
		actionObjNotif.target_object_id = request_id
		actionObjNotif.verb = "serh bildirdi"
		actionObjNotif.description = "commented on your request"
		actionObjNotif.timestamp = timezone.now()
		actionObjNotif.public = 1
		actionObjNotif.actor_content_type_id = 3
		actionObjNotif.recipient_id = profile.objects.filter(id=requestProfileID[0]).values_list("user_id",flat=True)[0]
		actionObjNotif.deleted = 0
		actionObjNotif.emailed = 0
		actionObjNotif.data = ""
		actionObjNotif.save()

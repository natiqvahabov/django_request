from django.contrib.auth.models import User
from profiles.models import profile
from database.models import ScAns
from django import template
from datetime import datetime
import dateutil.parser
import dateutil
from database.models import ScRequestsCategories,ScCategories,ScAns
import sys
import os.path

#!/usr/bin/env python
# -*- coding: utf-8 -*-

register = template.Library()

@register.filter(name='to_date')
def to_date(value):
	return dateutil.parser.parse(value)

@register.filter(name='cool_date')
def cool_date(value):
	date = datetime.strptime(value, '%Y-%m-%d %H:%M:%S.%f')
	return date

@register.filter(name='get_username')
def get_username(value):
	return User.objects.filter(id=value).values_list('username',flat=True)[0]

@register.filter(name='get_category')
def get_category(value):
	cID = ScRequestsCategories.objects.filter(req_id=value).values_list('cat_id',flat=True)
	return ScCategories.objects.filter(id=cID).values_list('name',flat=True)[0]

@register.filter(name='get_profile')
def get_profile(value):
	prof_id = profile.objects.filter(id=value).values_list('user_id',flat=True)[0]
	return User.objects.filter(id=prof_id).values_list('username',flat=True)[0]

@register.filter(name='get_email')
def get_profile(value):
	email = ScAns.objects.filter(username=value).values_list('email',flat=True)
	if email is None:
		contact = ScAns.objects.filter(username=value).values_list('internal_tel_num',flat=True)
		return contact
	else:
		return email[0]

@register.filter(name='get_internal_phone')
def get_internal_phone(value):
	contact = ScAns.objects.filter(username=value).values_list('internal_tel_num',flat=True)[0]
	if contact:
		return contact
	else:
		return "Daxili nomre elave edilmeyib"

@register.filter(name='to_read')
def to_read(value):
	print value

@register.filter(name='getNotificationName')
def getNotificationName(value):
	print unicode(value)
	return

@register.filter(name='getLocalTimeDifference')
def getLocalTimeDifference(value):
	value = value.replace('weeks','h'+u'\u0259'+'ft'+u'\u0259').replace('week','h'+u'\u0259'+'ft'+u'\u0259').replace('minutes','d'+u'\u0259'+'qiq'+u'\u0259').replace('minute','d'+u'\u0259'+'qiq'+u'\u0259').replace('hours','saat').replace('hour','saat').replace('days','g'+u'\xfc'+'n').replace('day','g'+u'\xfc'+'n')
	return value

@register.filter(name='getNotifUser')
def getNotifUser(value):
	return unicode(value).split(' ', 1)[0]

@register.filter(name='getFileName')
def getFileName(value):
	extension = os.path.basename(value)
	return extension

@register.filter(name='shortName')
def shortName(value):
	if len(value) > 40:
		return value[0:40]+ "..."
	else:
		return value

@register.filter(name='convert_utf8')
def convert_utf8(value):
	return value.replace(unichr(198),unichr(399)).replace(u'\xc4\xb0',unichr(73)).replace(u'\xc9\u2122',u'\u0259').replace(u'\xc4\xb1', u'\u0131').replace(u'\xc3\xbc',u'\xfc').replace(u'\xc3\xb6',u'\xf6').replace(u'\xc5\u0178',u'\u015f').replace(u'\xc4\u0178',u'\u011f').replace(u'\xc3\xa7',u'\xe7').replace(u'\xc3\u2013',u'\xd6').replace(u'\xc5\u017e',u'\u015e').replace(u'\xc3\u0153',u'\xdc')



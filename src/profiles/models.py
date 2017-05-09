from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from django.conf import settings
from database.models import ScAns
from allauth.account.signals import user_logged_in, user_signed_up
from django.db.models.signals import post_save 
from django.dispatch import receiver

class profile(models.Model):
	user             = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,null=True,blank=True)
	name             = models.CharField(default="name",max_length=120)
	id               = models.CharField(primary_key=True,max_length=30,default="23")
	password         = models.CharField(max_length=120, default="department", blank=True, null=True)
	surname          = models.CharField(default="surname",max_length=120)
	fathername       = models.CharField(default="father name",max_length=120)
	department       = models.CharField(max_length=120, default="department", blank=True, null=True)
	par_us_name      = models.CharField(max_length=120, default="parent user name", blank=True, null=True)
	position         = models.CharField(max_length=120, default="position",null=True,blank=True)
	role             = models.CharField(max_length=2, default="4")
	ip               = models.CharField(max_length=20, default="192.168.1.1",null=True,blank=True)
	notif_ask        = models.CharField(max_length=3, blank=True, null=True)
	notif_answer     = models.CharField(max_length=3, blank=True, null=True)
	internal_tel_num = models.CharField(max_length=30, blank=True, null=True)
	mob_tel_num      = models.CharField(max_length=50, blank=True, null=True)
	image            = models.CharField(max_length=300, blank=True, null=True)

	def __unicode__(self):
		return self.name



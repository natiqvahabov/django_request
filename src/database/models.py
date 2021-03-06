# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = True` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.


# DATABASElerin primary keylerni yoxlamaq lazimdir.

# coding=utf8

from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from django.conf import settings
import os
import datetime

# Create your models here.
class ScComments(models.Model):
	id = models.FloatField(blank=True, null=True, primary_key=True)
	req_id = models.FloatField(blank=True, null=True)
	ans_id = models.CharField(max_length=200, blank=True, null=True)
	ins_date = models.CharField(max_length=40, blank=True, null=True)
	file_path = models.CharField(max_length=2000, blank=True, null=True)
	comment_text = models.CharField(max_length=4000, blank=True, null=True)

	class Meta:
		managed = True
		db_table = 'sc_comments'

	def __getitem__(id):
		return self.name

	def __str__(id):
		return self.name

	def __unicode__(self):
		return unicode(self).encode('utf-8')


def user_directory_path(instance, filename):
	i = datetime.datetime.now()
	return '{0}'.format(instance.path)


class Document(models.Model):
	id = models.AutoField(primary_key=True)
	user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,null=True,blank=True)
	path = models.CharField(max_length=255,blank=True, null=True)
	request_id = models.CharField(max_length=255)
	document = models.FileField(upload_to=user_directory_path)
	uploaded_at = models.DateTimeField(auto_now_add=True)


class ScAction(models.Model):
	id = models.FloatField(primary_key=True)
	name = models.CharField(max_length=20, blank=True, null=True)

	class Meta:
		managed = True
		db_table = 'sc_action'

	def __getitem__(id):
		return self.name

	def __unicode__(self):
		return unicode(self).encode('utf-8')


class ScAns(models.Model):
	id = models.FloatField(primary_key=True)
	user = models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
	ip = models.CharField(max_length=20, blank=True, null=True)
	ad = models.CharField(max_length=20, blank=True, null=True)
	soyad = models.CharField(max_length=20, blank=True, null=True)
	username = models.CharField(max_length=200, blank=True, null=True)
	password = models.CharField(max_length=200, blank=True, null=True)
	role = models.FloatField(blank=True, null=True)
	email = models.CharField(max_length=2000, blank=True, null=True)
	parent_username = models.CharField(max_length=2000, blank=True, null=True)
	notif_ask = models.CharField(max_length=3, blank=True, null=True)
	notif_answer = models.CharField(max_length=3, blank=True, null=True)
	department = models.CharField(max_length=100, blank=True, null=True)
	position = models.CharField(max_length=50, blank=True, null=True)
	internal_tel_num = models.CharField(max_length=30, blank=True, null=True)
	mob_tel_num = models.CharField(max_length=50, blank=True, null=True)
	image = models.CharField(max_length=300, blank=True, null=True)
	ata_adi = models.CharField(max_length=20, blank=True, null=True)

	class Meta:
		managed = True
		db_table = 'sc_ans'

	def __getitem__(id):
		return self.name

	def __unicode__(self):
		return unicode(self).encode('utf-8')


class ScAnsAction(models.Model):
	id = models.FloatField(primary_key=True)
	user_id = models.FloatField()
	action_id = models.FloatField()
	req_id = models.FloatField()
	a_date = models.DateField()

	class Meta:
		managed = True
		db_table = 'sc_ans_action'

	def __getitem__(id):
		return self.name

	def __unicode__(self):
		return unicode(self).encode('utf-8')


class ScAnsActionNew(models.Model):
	id = models.AutoField(primary_key=True)
	user_id = models.IntegerField()
	action_id = models.IntegerField()
	req_id = models.IntegerField()
	a_date = models.DateField()

	class Meta:
		managed = True
		db_table = 'sc_ans_action_new'

	def __getitem__(id):
		return self.name

	def __unicode__(self):
		return unicode(self).encode('utf-8')


class ScActionNotif(models.Model):
	id = models.AutoField(primary_key=True)
	action_id = models.IntegerField(blank=True, null=True)
	user_id = models.IntegerField(blank=True, null=True)
	notif = models.CharField(max_length=20, blank=True, null=True)

	class Meta:
		managed = True
		db_table = 'sc_action_notif'

	def __getitem__(id):
		return self.name

	def __unicode__(self):
		return unicode(self).encode('utf-8')


class ScAnsActionNotif(models.Model):
	id = models.FloatField(primary_key=True)
	user_id = models.FloatField(blank=True, null=True)
	action_id = models.FloatField(blank=True, null=True)
	req_id = models.FloatField(blank=True, null=True)
	who_see = models.CharField(max_length=50, blank=True, null=True)
	notif = models.CharField(max_length=20, blank=True, null=True)

	class Meta:
		managed = True
		db_table = 'sc_ans_action_notif'

	def __getitem__(id):
		return self.name

	def __unicode__(self):
		return unicode(self).encode('utf-8')


class ScAnsCategories(models.Model):
	id = models.FloatField(blank=True, null=True,primary_key=True)
	ans_username = models.CharField(max_length=200, blank=True, null=True)
	cat_id = models.FloatField(blank=True, null=True)
	utype = models.CharField(max_length=2, blank=True, null=True)

	class Meta:
		managed = True
		db_table = 'sc_ans_categories'

	def __getitem__(id):
		return self.name

	def __str__(id):
		return self.name

	def __unicode__(self):
		return unicode(self).encode('utf-8')


class ScAnsParent(models.Model):
	id = models.FloatField(blank=True, null=True,primary_key=True)
	parent_name = models.CharField(max_length=200)
	child_name = models.CharField(max_length=200)

	class Meta:
		managed = True
		db_table = 'sc_ans_parent'

	def __getitem__(id):
		return self.name

	def __unicode__(self):
		return unicode(self).encode('utf-8')


class ScCategories(models.Model):
	id = models.FloatField(primary_key=True)
	name = models.CharField(max_length=2000, blank=True, null=True)
	slug = models.CharField(max_length=200, blank=True, null=True)

	class Meta:
		managed = True
		db_table = 'sc_categories'

	def __getitem__(id):
		return self.name

	def __str__(id):
		return self.name

	def __unicode__(self):
		return unicode(self).encode('utf-8')


class ScComments2(models.Model):
	id = models.FloatField(primary_key=True)
	req_id = models.FloatField(blank=True, null=True)
	ans_id = models.CharField(max_length=200, blank=True, null=True)
	ins_date = models.CharField(max_length=40, blank=True, null=True)
	file_path = models.CharField(max_length=2000, blank=True, null=True)
	comment_text = models.TextField(blank=True, null=True)  # This field type is a guess.
	comment_text2 = models.CharField(max_length=4000, blank=True, null=True)

	class Meta:
		managed = True
		db_table = 'sc_comments2'


class ScCommentsPrivacy(models.Model):
	id = models.FloatField(primary_key=True)
	comment_id = models.FloatField(blank=True, null=True)
	ans_id = models.CharField(max_length=200, blank=True, null=True)
	com_act = models.CharField(max_length=20, blank=True, null=True)

	class Meta:
		managed = True
		db_table = 'sc_comments_privacy'


class ScLogs(models.Model):
	id = models.FloatField(primary_key=True)
	name = models.CharField(max_length=200, blank=True, null=True)
	value = models.CharField(max_length=200, blank=True, null=True)
	logtype = models.CharField(max_length=200, blank=True, null=True)
	logdate = models.CharField(max_length=200, blank=True, null=True)

	class Meta:
		managed = True
		db_table = 'sc_logs'


class ScNotifyList(models.Model):
	id = models.FloatField(blank=True, null=True, primary_key=True)
	email = models.CharField(max_length=200, blank=True, null=True)
	parent = models.CharField(max_length=200, blank=True, null=True)
	notify = models.CharField(max_length=20, blank=True, null=True)

	class Meta:
		managed = True
		db_table = 'sc_notify_list'


class ScRequestTags(models.Model):
	id = models.FloatField(primary_key=True)
	tagged_user = models.CharField(max_length=50, blank=True, null=True)
	req_id = models.FloatField(blank=True, null=True)
	view_status = models.CharField(max_length=30, blank=True, null=True)
	tagged_date = models.CharField(max_length=20, blank=True, null=True)
	who_tagged = models.CharField(max_length=50, blank=True, null=True)

	class Meta:
		managed = True
		db_table = 'sc_request_tags'

	def __getitem__(id):
		return self.name

	def __str__(id):
		return self.name

	def __unicode__(self):
		return unicode(self).encode('utf-8')


class ScRequests(models.Model):
	id = models.FloatField(primary_key=True)
	title = models.CharField(max_length=500, blank=True, null=True)
	description = models.CharField(max_length=4000, blank=True, null=True)
	rtype = models.CharField(max_length=100, blank=True, null=True)
	file_path = models.CharField(max_length=1000, blank=True, null=True)
	status = models.CharField(max_length=50, blank=True, null=True)
	solution_desc = models.CharField(max_length=4000, blank=True, null=True)
	ans_ip = models.CharField(max_length=20, blank=True, null=True)
	sender = models.CharField(max_length=200, blank=True, null=True)
	ins_date = models.CharField(max_length=40, blank=True, null=True)

	class Meta:
		managed = True
		db_table = 'sc_requests'

	def __getitem__(id):
		return self.name

	def __str__(id):
		return self.name

	def __unicode__(self):
		return unicode(self).encode('utf-8')


class ScRequestsCategories(models.Model):
	id = models.FloatField(primary_key=True)
	req_id = models.FloatField(blank=True, null=True)
	cat_id = models.FloatField(blank=True, null=True)

	class Meta:
		managed = True
		db_table = 'sc_requests_categories'

	def __getitem__(id):
		return self.name

	def __str__(id):
		return self.name

	def __unicode__(self):
		return unicode(self).encode('utf-8')


class ScSubCategories(models.Model):
	id = models.IntegerField(primary_key=True)
	name = models.CharField(max_length=2000)
	slug = models.CharField(max_length=150)
	category_id = models.IntegerField()

	class Meta:
		managed = True
		db_table = 'sc_sub_categories'


class SctaCats(models.Model):
	id = models.FloatField(primary_key=True)
	name = models.CharField(max_length=2000, blank=True, null=True)
	req_same = models.CharField(max_length=200, blank=True, null=True)

	class Meta:
		managed = True
		db_table = 'scta_cats'


class SctaCommentNotif(models.Model):
	id = models.FloatField(primary_key=True)
	user_name = models.CharField(max_length=30, blank=True, null=True)
	comment_id = models.FloatField(blank=True, null=True)
	status = models.CharField(max_length=20, blank=True, null=True)
	req_id = models.FloatField(blank=True, null=True)

	class Meta:
		managed = True
		db_table = 'scta_comment_notif'


class SctaComments(models.Model):
	id = models.FloatField(blank=True, null=True, primary_key=True)
	req_id = models.FloatField(blank=True, null=True)
	ans_id = models.CharField(max_length=200, blank=True, null=True)
	ins_date = models.CharField(max_length=40, blank=True, null=True)
	file_path = models.CharField(max_length=2000, blank=True, null=True)
	comment_text = models.CharField(max_length=4000, blank=True, null=True)

	class Meta:
		managed = True
		db_table = 'scta_comments'


class SctaLogs(models.Model):
	id = models.FloatField(primary_key=True)
	name = models.CharField(max_length=200, blank=True, null=True)
	value = models.CharField(max_length=200, blank=True, null=True)
	logtype = models.CharField(max_length=200, blank=True, null=True)
	logdate = models.CharField(max_length=200, blank=True, null=True)

	class Meta:
		managed = True
		db_table = 'scta_logs'


class SctaTasks(models.Model):
	id = models.FloatField(primary_key=True)
	title = models.CharField(max_length=500, blank=True, null=True)
	rtype = models.CharField(max_length=100, blank=True, null=True)
	status = models.CharField(max_length=200, blank=True, null=True)
	ans_ip = models.CharField(max_length=20, blank=True, null=True)
	sender = models.CharField(max_length=200, blank=True, null=True)
	ins_date = models.CharField(max_length=40, blank=True, null=True)
	sol_date = models.CharField(max_length=40, blank=True, null=True)
	ttype = models.CharField(max_length=200, blank=True, null=True)
	description = models.CharField(max_length=4000, blank=True, null=True)
	file_path = models.CharField(max_length=1000, blank=True, null=True)
	req_status = models.CharField(max_length=50, blank=True, null=True)

	class Meta:
		managed = True
		db_table = 'scta_tasks'


class SctaTasksCats(models.Model):
	id = models.FloatField(primary_key=True)
	req_id = models.FloatField(blank=True, null=True)
	cat_id = models.FloatField(blank=True, null=True)

	class Meta:
		managed = True
		db_table = 'scta_tasks_cats'


class SctaTips(models.Model):
	id = models.FloatField(blank=True, null=True,primary_key=True)
	name = models.CharField(max_length=500, blank=True, null=True)

	class Meta:
		managed = True
		db_table = 'scta_tips'


class SctaUsers(models.Model):
	id = models.FloatField(primary_key=True)
	ip = models.CharField(max_length=20, blank=True, null=True)
	ad = models.CharField(max_length=20, blank=True, null=True)
	soyad = models.CharField(max_length=20, blank=True, null=True)
	username = models.CharField(max_length=200, blank=True, null=True)
	password = models.CharField(max_length=200, blank=True, null=True)
	role = models.FloatField(blank=True, null=True)
	email = models.CharField(max_length=2000, blank=True, null=True)
	notif_ask = models.CharField(max_length=3, blank=True, null=True)
	notif_answer = models.CharField(max_length=3, blank=True, null=True)
	department = models.CharField(max_length=50, blank=True, null=True)
	position = models.CharField(max_length=50, blank=True, null=True)
	internal_tel_num = models.CharField(max_length=30, blank=True, null=True)
	mob_tel_num = models.CharField(max_length=50, blank=True, null=True)
	image = models.CharField(max_length=300, blank=True, null=True)
	ata_adi = models.CharField(max_length=20, blank=True, null=True)
	parent_username = models.CharField(max_length=20, blank=True, null=True)

	class Meta:
		managed = True
		db_table = 'scta_users'


class SctaUsersCats(models.Model):
	id = models.FloatField(blank=True, null=True,primary_key=True)
	ans_username = models.CharField(max_length=200, blank=True, null=True)
	cat_id = models.FloatField(blank=True, null=True)
	utype = models.CharField(max_length=2, blank=True, null=True)

	class Meta:
		managed = True
		db_table = 'scta_users_cats'

from django.db.models.signals import post_save
from notifications.signals import notify
from database.models import ScComments


def send_notification(request,request_id,comment):
	post_save.connect(my_handler, sender=request.user)
	notify.send(request.user, recipient=request.user, verb='commented on your request')

	print "reqID " + request_id

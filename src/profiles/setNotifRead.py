from notifications.models import Notification
import json

def setNotifRead(request, notif_id):
	notifObject = Notification.objects.filter(pk=notif_id)[0]
	notifObject.mark_as_read()
	return
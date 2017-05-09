from django.contrib.auth.models import User
from django.contrib.auth.models import AnonymousUser
from database.models import ScAns
import socket
from django.shortcuts import render
from profiles.models import profile
from django.contrib.auth import authenticate, login

def get_ip_address(request):
	#print(socket.gethostbyname(socket.getfqdn()))
	
	x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
	if x_forwarded_for:
		ip = x_forwarded_for.split(',')[0]
	else:
		ip = request.META.get('REMOTE_ADDR')    ### Real IP address of client Machine
	return ip

# Login with IP address
def login_ip_address(request,ipAdd,user):
	if user == AnonymousUser():
		remoteip = ipAdd
		try:
			profile_user  = profile.objects.get(ip=remoteip)
			user_logged   = profile_user.user
			user_password = profile_user.password
			user_username = user_logged.username

			user = authenticate(username = user_username, password = user_password)
			if profile_user is not None:
				login(request, user)

		except profile.DoesNotExist:
			context = locals()
			template = "account/login.html"
			return render(request,template,context)
	return None
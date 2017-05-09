from django.shortcuts import render
from django.conf import settings
from .forms import contactForm
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.db import models

# Create your views here.
def contact(request):
	title = "Content"
	form = contactForm(request.POST or None)
	confirm_message=""

	context = {'title': title, 'form': form,'confirm_message':confirm_message}

	if form.is_valid():
		print "here"
		name = form.cleaned_data['name']
		comment = form.cleaned_data['comment']

		subject = "SOCARdan ismaric"
		message = "%s %s" % (comment, name)
		emailTo = [form.cleaned_data['email']]
		emailFrom = "noreplay@socar.az"
		send_mail(
                  subject,
                  message,
                  emailFrom,
                  emailTo,
                  fail_silently=False,
        )
        print "here 2"
        title = "Thanks"
        confirm_message = "Thanks for the message. We will get right back to you."

	template = "contact.html"
	return render(request,template,context)
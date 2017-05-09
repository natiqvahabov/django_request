"""Django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from profiles import views as profile_views
from contact import views as contact_views
import debug_toolbar
from django.conf.urls import (handler400, handler403, handler404, handler500)

import notifications.urls

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', profile_views.home, name='home'),
    url(r'^search/$', profile_views.search, name='search'),
    url(r'^about/$', profile_views.about, name='about'),
    url(r'^about/addComment/$', profile_views.addComment, name='addComment'),
    url(r'^about/addRequest/$', profile_views.addRequest, name='addRequest'),
    url(r'^getCatRequests/$', profile_views.getCatRequests, name='getCatRequests'),
    url(r'^updateUserProfile/$', profile_views.updateUserProfile, name='updateUserProfile'),   
    url(r'^getSentRequests/$', profile_views.getSentRequests, name='getSentRequests'),
    url(r'^getParentRequests/$', profile_views.getParentRequests, name='getParentRequests'),
    url(r'^otherRequests/$', profile_views.otherRequests, name='otherRequests'),
    url(r'^about/updateRequestDone/$', profile_views.updateRequestDone, name='updateRequestDone'),
    url(r'^about/updateRequestLocked/$', profile_views.updateRequestLocked, name='updateRequestLocked'),
    url(r'^about/tagUser/$', profile_views.tagUser, name='tagUser'),
    url(r'^profile/$', profile_views.userProfile, name='profile'),
    url(r'^request/$', profile_views.makeRequest, name='makeRequest'),
    url(r'^contact/$', contact_views.contact, name='contact'),
    url(r'^inbox/notifications/', include(notifications.urls, namespace='notifications'), name="notifications"),
    url(r'^about/$', profile_views.about, name='about'),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^debug/', include(debug_toolbar.urls)),
]

if True:
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
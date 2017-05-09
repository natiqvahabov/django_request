from django.contrib import admin
from profiles.models import profile
from django.contrib.auth.admin import UserAdmin
from database.models import ScAns
from django.contrib.auth.models import User

class profileAdmin(admin.ModelAdmin):
	fk_name = 'id'
	class Meta:
		model=profile

admin.site.register(profile,profileAdmin)


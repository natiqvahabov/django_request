from django.contrib import admin
from database.models import Document,ScRequests

# Register your models here.

class DocumentFiles(admin.ModelAdmin):
	fk_name = 'id'
	class Meta:
		model=Document

admin.site.register(Document,DocumentFiles)

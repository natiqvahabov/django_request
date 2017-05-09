from django import forms
from database.models import ScComments,Document,ScAnsAction,ScRequests

class CommentForm(forms.ModelForm):
	class Meta:
		model = ScComments
		fields = "__all__"

class DocumentForm(forms.ModelForm):
	class Meta:
		model = Document
		fields = "__all__"

class RequestForm(forms.ModelForm):
	class Meta:
		model = ScRequests
		fields = "__all__"

class ActionForm(forms.ModelForm):
	class Meta:
		model = ScAnsAction
		fields = "__all__"
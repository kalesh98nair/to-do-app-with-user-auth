from django import forms
from django.forms import ModelForm

from .models import *


class TaskForm(forms.ModelForm):
	title = forms.CharField(label='', widget = forms.TextInput(attrs = {'placeholder':'Add new note...'}))
	#id = forms.CharField(widget=forms.TextInput(attrs = { "class": "form-control"}))
	class Meta:
		model = Task
		fields = '__all__'

from django import forms
from django.forms import ModelForm
from .models import Post

class PostForm(ModelForm):
	class Meta:
		model=Post
		fields=['title','body']

		widgets={
		'body':forms.Textarea
		}
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.edit import ModelFormMixin
from django.views.generic.list import ListView
from .models import Post
from .forms import PostForm

class Home(ListView):
	model=Post
	template_name='crud/home.html'

	def get_queryset(self):
		queryset=Post.objects.all()
		queryset=queryset.order_by('updated_at', 'created_at')
		queryset=queryset[:9]
		return queryset

class Create(CreateView):
	model=Post
	form_class=PostForm
	template_name_suffix='_create'
	success_url='/crud/home'

class Delete(DeleteView):
	model=Post
	template_name_suffix='_delete'
	success_url='/crud/home'

class Update(UpdateView):
	model=Post
	form_class=PostForm
	template_name_suffix='_update'
	success_url='/crud/home'

from . import views
from django.urls import path

urlpatterns=[
	path('create/', views.Create.as_view(), name='CreateView'),
	path('delete/<pk>/',views.Delete.as_view(), name='DeleteView'),
	path('update/<pk>/',views.Update.as_view(), name='UpdateView'),
	path('home/', views.Home.as_view(), name='HomeView')
]
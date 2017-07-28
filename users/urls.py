from django.conf.urls import url
from . import views

app_name = 'users'
urlpatterns = [
	url(r'^get/$', views.getUsers, name='get'),
	url(r'^create/$', views.createUsers, name='create'),
	url(r'^update/$', views.updateUsers, name='update'),
	url(r'^delete/$', views.deleteUsers, name='delete'),
	url(r'^all/$', views.allUsers, name='all'),
	url(r'^login/$', views.loginView, name='login'),
	url(r'^dashboard/$', views.loginUser, name='loggedin'),
]
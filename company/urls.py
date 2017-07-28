from django.conf.urls import url
from . import views

app_name = 'company'
urlpatterns = [
	url(r'^get/$', views.getCompany, name='get'),
	url(r'^create/$', views.createCompany, name='create'),
	url(r'^update/$', views.updateCompany, name='update'),
	url(r'^delete/$', views.deleteCompany, name='delete'),
	url(r'^all/$', views.allCompany, name='all'),
]
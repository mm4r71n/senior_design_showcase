from django.urls import path

from . import views 
#can use 'index' to link pages
urlpatterns = [
	path('', views.index, name = 'index'),
	path('about', views.about, name = 'about'),
]
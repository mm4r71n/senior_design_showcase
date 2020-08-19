from django.urls import path

from . import views 
#can use 'index' to link pages
urlpatterns = [
	path('', views.index, name = 'listings'),
	path('<int:listing_id>', views.listing, name = 'listing'),
	#calls search method
	path('search', views.search, name = 'search'),

]
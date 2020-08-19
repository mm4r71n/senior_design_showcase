
from django.contrib import admin
from django.urls import path, include
#for media files to show up on front end 
from django.conf import settings
from django.conf.urls.static import static



urlpatterns =[
	path('', include('pages.urls')),
	path('listings/', include('listings.urls')),
	path('contacts/', include('contacts.urls')),
    path('admin/', admin.site.urls),


  #for media files to show up on front end  
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
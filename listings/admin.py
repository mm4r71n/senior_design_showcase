from django.contrib import admin

# Register your models here.

# must import same name as in models.py- Listing
from .models import Listing


class ListingAdmin(admin.ModelAdmin):
	list_display = ('id', 'title', 'is_published', 'price', 'list_date', 'sqft')
	#sets links to get to listing 
	list_display_links = ('id', 'title')
	#filters by list date
	list_filter = ('list_date',)
	list_editable = ('is_published',)
	#search fields
	search_fields = ('title', 'description', 'address' , 'city', 'state', 'zipcode','price')
	#pagination
	list_per_page = 25


# will create Listing in Django admin portal
admin.site.register(Listing, ListingAdmin)






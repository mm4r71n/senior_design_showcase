from django.shortcuts import render
from django.http import HttpResponse 
from listings.choices import price_choices, bedroom_choices, state_choices

from listings.models import Listing 
# Create your views here.

def index(request):				# will show the three latest listings on home/index page
	listings = Listing.objects.order_by('-list_date').filter(is_published = True)[:3]

	context = { 

		'listings': listings,	
		'state_choices': state_choices,
		'bedroom_choices': bedroom_choices,
		'price_choices': price_choices

	}
	#passing into index template
	return render(request, 'pages/index.html', context)

def about(request):
	return  render(request, 'pages/about.html')



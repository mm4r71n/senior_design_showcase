from django.test import SimpleTestCase
from django.urls import reverse, resolve 
from listings.views import index, listing, search

class TestUrls(SimpleTestCase):

    #test if the home page URL is being called properly
    def test_list_url_is_resolved(self):
        url = reverse('listings')
        print(resolve(url))
        self.assertEquals(resolve(url).func, index)
    
    #test if the search page URL is being called properly
    def test_search_url_is_resolved(self):
        url = reverse('search')
        print(resolve(url))
        self.assertEquals(resolve(url).func, search)

    #test if the listing page URL is being called properly with argument
    def test_listing_url_is_resolved(self):
        url = reverse('listing', args = [5])
        print(resolve(url))
        self.assertEquals(resolve(url).func, listing)

######################## FINISHED  URL TESTING  #########################################


######################## TESTING VIEWS #######################################


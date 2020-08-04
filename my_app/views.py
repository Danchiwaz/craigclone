import requests
from requests.compat import quote_plus
from django.shortcuts import render
from . import models
from bs4 import BeautifulSoup

# Create your views here.

BASE_CRAIGSLIST_URL='https://kenya.craigslist.org/search/bbb?query={}&sort=rel'
BASE_IMG_URL= 'https://images.craigslist.org/{}_300*300.jpg'


def home(request):
	return render(request, 'base.html')


def new_search(request):
	# fetching the data from the from
	search=request.POST.get('search')
	models.Search.objects.create(search=search)
	final_url= BASE_CRAIGSLIST_URL.format(quote_plus(search))
	response=requests.get(final_url)
	data=response.text
	# parsing the html data to BeautifulSoup

	soup= BeautifulSoup(data, features='html.parser')
	post_listings=soup.find_all('li', { 'class':'result-row' })
	
	
	final_postings=[]

	for post in post_listings:
		post_title= post.find(class_="result-title").text
		post_url= post.find('a').get('href')

		if post.find(class_='result-price'):
			post_price= post.find(class_='result-price').text
		else:
			post_price='N/A'


		if post.find(class_='result-image').get('data-ids'):
			post_img_id= post.find(class_='result-image').get('data-ids').split(',')[0].split(' : ')
			
			post_img_url=BASE_IMG_URL.format(post_img_url)
		
		else:
			post_img_url='https://craigslist.org/images/peace.jpg'




			
			

		

	final_postings.append((post_title, post_url, post_price, post_img_url))	

	
	
	
	
	
	
	staff_for_frontend={
	   'search': search,
	   'final_postings': final_postings,
	   
	}
	return render(request, 'my_app/new_search.html', staff_for_frontend)

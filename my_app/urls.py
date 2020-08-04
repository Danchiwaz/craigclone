from django.urls import path
from . import views

# This are the urls for my_app app 


urlpatterns= [
   path('', views.home, name='home'),
   path('new_search', views.new_search, name='new_search'),

]
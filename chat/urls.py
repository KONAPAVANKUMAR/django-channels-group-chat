from django.urls import path
from .views import *

urlpatterns = [
	path('',homepageview),
	path('room/',roomview,name = 'room')
]
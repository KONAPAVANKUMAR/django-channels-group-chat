from django.shortcuts import render
from .models import ChatModel
# Create your views here.
def homepageview(request):
	return render(request,'index.html')

def roomview(request):
	room_no = request.POST['room_no']
	name = request.POST['name']
	messages = []
	for eachobj in ChatModel.objects.filter(room_no = room_no):
		messages.append(eachobj.message)
	return render(request,'room.html',{'room_no' : room_no,'name' : name,'messages':messages})
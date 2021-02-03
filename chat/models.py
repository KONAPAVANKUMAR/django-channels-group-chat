from django.db import models

# Create your models here.
class ChatModel(models.Model):
	room_no = models.CharField(max_length = 128)
	message = models.TextField()
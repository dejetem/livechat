from django.contrib import admin

# Register your models here.
from .models import RoomUsers, Message

admin.site.register(RoomUsers)
admin.site.register(Message)
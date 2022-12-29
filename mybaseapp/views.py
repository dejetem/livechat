from django.shortcuts import render
from django.http import JsonResponse
import random
import time
import json
from agora_token_builder import RtcTokenBuilder
from .models import RoomUsers
from django.views.decorators.csrf import csrf_exempt
from dotenv import load_dotenv
import os

load_dotenv()

# Create your views here.
def home(request):
    return render(request, 'home.html')

def lobby(request):
    return render(request, 'lobby.html')

def room(request):
    return render(request, 'room.html')

def getToken(request):
    appId = os.getenv('APP_ID')
    appCertificate = os.getenv('APP_CERTIFICATE')
    channelName = request.GET.get('channel')
    uid = random.randint(1, 230)
    expirationTimeInSeconds = 3600 * 24
    currentTimeStamp = time.time()
    privilegeExpiredTs = currentTimeStamp + expirationTimeInSeconds
    role = 1

    token = RtcTokenBuilder.buildTokenWithUid(appId, appCertificate, channelName, uid, role, privilegeExpiredTs)

    return JsonResponse({'token': token, 'uid': uid}, safe=False)


@csrf_exempt
def createUser(request):
    data = json.loads(request.body)
    member, created = RoomUsers.objects.get_or_create(
        name=data['name'],
        uid=data['UID'],
        room_name=data['room_name']
    )

    return JsonResponse({'name':data['name']}, safe=False)


def getUser(request):
    uid = request.GET.get('UID')
    room_name = request.GET.get('room_name')

    member = RoomUsers.objects.get(
        uid=uid,
        room_name=room_name,
    )
    name = member.name
    return JsonResponse({'name':member.name}, safe=False)



@csrf_exempt
def deleteUser(request):
    data = json.loads(request.body)
    member = RoomUsers.objects.get(
        name=data['name'],
        uid=data['UID'],
        room_name=data['room_name']
    )
    member.delete()
    return JsonResponse('Member deleted', safe=False)
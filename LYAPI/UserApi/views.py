
from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework import status
from UserApi.models import CxxUser
# Create your views here.


class UserView(View):
    def post(self,request):
        data = JSONParser().parse(request)
        instance= CxxUser.objects.get(u_account=data['u_account'])
        return JsonResponse(data=instance,safe=False)
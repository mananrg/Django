from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
# Create your views here.
def home(request):
    return JsonResponse({"info":'Django React Course',"name":'manan'})
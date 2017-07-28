from django.http import Http404, JsonResponse
from django.shortcuts import render

def getUsers(request):
	return JsonResponse({'foo':'bar'})

def createUsers(request):
	return JsonResponse({'foo':'bar'})

def updateUsers(request):
	return JsonResponse({'foo':'bar'})

def deleteUsers(request):
	return JsonResponse({'foo':'bar'})
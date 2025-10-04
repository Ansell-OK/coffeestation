from django.shortcuts import render
from django.http import HttpResponse


def profilePage(request):
    return HttpResponse("Profile Page")
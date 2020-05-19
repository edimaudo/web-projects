from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request, "coins/index.html", 
    {'title': 'All Coins Price'})
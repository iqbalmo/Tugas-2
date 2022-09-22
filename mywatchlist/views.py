from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import render
from mywatchlist.models import MyWatchList

# Create your views here.

def show_mywatchlist(request):
    data_film = MyWatchList.objects.all()
    context = {
        'list_film': data_film,
        'nama': 'Mochammad Iqbal',
        'npm': '2006531056'
    }
    return render(request, "mywatchlist.html", context)

def show_mywatchlist_xml(request):
    data = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_mywatchlist_json(request):
    data = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
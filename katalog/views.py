from django.shortcuts import render
from katalog.models import CatalogItem

# TODO: Create your views here.
def show_katalog(request):
    data_katalog = CatalogItem.objects.all()
    context = {
    'list_barang': data_katalog,
    'nama': 'Mochammad Iqbal',
    'npm': '2006531056'
    }
    return render(request, "katalog.html", context)
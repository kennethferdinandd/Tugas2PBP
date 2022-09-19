from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from mywatchlist.models import MyWatchlist

# TODO: Create your views here.

def show_xml(data) :
    data = MyWatchlist.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(data) :
    data = MyWatchlist.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_mywatchlist(request):
    return render(request, "mywatchlist.html", context)

def show_json_by_id(request, id) :
    data = MyWatchlist.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id) :
    data = MyWatchlist.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")


data_mywatchlist = MyWatchlist.objects.all()
context = {
    'list_mywatchlist': data_mywatchlist,
    'nama': 'Kenneth',
    'id': '2106750282',
}
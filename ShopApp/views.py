from django.shortcuts import render
from .services import sale
from django.http import HttpResponse
# Create your views here.
def index(request):
    dict1 = dict() #это пока
    return render(request, "ShopApp/index.html", dict1)
    
def buy(request):
    if request.method == "POST":
        sale(request)
        return HttpResponse("Спасибо, {0}".format(request.POST["name"]))
    else:
        return render(request, "ShopApp/buyForm.html")
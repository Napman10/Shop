from django.shortcuts import render

# Create your views here.
def index(request):
    dict1 = dict() #это пока
    return render(request, "ShopApp/index.html", dict1)
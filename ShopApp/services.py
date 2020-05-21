from django.shortcuts import render

# Create your views here.
def sale(request):
    prodId = request.GET.get("item", "")
    prod = Product.manager.get(id=prodId)
    prod.count-=1
    prod.save()
from django.shortcuts import render

# Create your views here.
def MyShop(request):
    return render(request,'budget.html')
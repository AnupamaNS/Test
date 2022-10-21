from django.shortcuts import render
from category.models import Category

# Create your views here.
def catreg(request):

    if request.method=="POST":
        ob = Category()
        ob.c_name = request.POST.get('cat')
        ob.save()
    return render(request,'category/Category.html')
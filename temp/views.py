from django.shortcuts import render

# Create your views here.
def temp(request):
    return render(request,'temp/main_home.html')

def admin(request):
    return render(request,'temp/admin.html')

def shop(request):
    return render(request,'temp/shop.html')

def user(request):
    return render(request,'temp/user.html')
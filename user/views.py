from django.shortcuts import render
from user.models import User
from login.models import Login

# Create your views here.
def userreg(request):
    if request.method=="POST":
        ob = User()
        ob.u_name = request.POST.get('usr')
        ob.password = request.POST.get('pwd')
        ob.email = request.POST.get('Email')
        ob.gender = request.POST.get('gen')
        ob.address = request.POST.get('adr')
        ob.contact = request.POST.get('ct')
        ob.status = "pending"
        ob.save()
        obj = Login()
        obj.username = ob.u_name
        obj.password = ob.password
        obj.type = "user"
        obj.u_id = ob.u_id
        obj.save()
    return render(request,'user/User.html')

from typing import Dict

from django.db.models import QuerySet
from django.shortcuts import render
from complaint.models import Complaint
from user.models import User

import datetime
# Create your views here.
def cmpreg(request):
    vv= request.session["u_id"]
    if request.method == "POST":
        ob = Complaint()
        ob.complaint = request.POST.get('cmp')
        ob.u_id = vv
        ob.reply = "Pending"
        ob.date = datetime.date.today()
        ob.time = datetime.datetime.now()
        ob.save()
    return render(request,'complaint/Complaint.html')

def viewcmp(request):
    ob = Complaint.objects.filter(reply='pending')
    context = {
        'obval': ob,
    }
    return render(request, 'complaint/view_complaint.html', context)

def mngcmp(request):
    # cc=request.session["u_id"]
    ob =Complaint.objects.filter()
    context = {
        'obval': ob,
    }
    return render(request, 'complaint/manage_complaint.html', context)

def reply(request,idd):
    ob= Complaint.objects.filter(cp_id=idd)
    context = {
        'obval': ob,
    }
    if request.method == "POST":
        ob = Complaint.objects.get(cp_id=idd)
        ob.reply = request.POST.get('reply')
        ob.save()
        return viewcmp(request)
    return render(request,'complaint/reply.html',context)

def viewrply(request):
    dd=request.session["u_id"]
    print(dd)
    ob = Complaint.objects.filter(u_id=dd)
    context = {
        'obval': ob,
    }
    return render(request,'complaint/view_reply.html',context)

from django.shortcuts import render
from ratin.models import Rating
from user.models import User
import datetime
# Create your views here.
def view_rating(request):
    objlist=Rating.objects.all()
    context={
        'objv':objlist,
    }
    return render(request, 'ratin/view_rating.html',context)

def rateshop(request):
    objlist=Rating.objects.all()
    context={
        'objv':objlist
    }
    return render(request, 'rating/ratingviewshop.html',context)

def postrate(request):
    cc=request.session["u_id"]
    if request.method=="POST":
        obj=Rating()
        obj.rating=request.POST.get('rating')
        obj.date=datetime.datetime.today()
        obj.time=datetime.datetime.now()
        obj.u_id=cc
        obj.save()
    return render(request, 'rating/ratepost.html')
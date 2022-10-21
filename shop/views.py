from django.shortcuts import render
from shop.models import Shop
from login.models import Login

# Create your views here.
def shopreg(request):
    if request.method=="POST":
        ob = Shop()
        ob.s_name = request.POST.get('sname')
        ob.email = request.POST.get('Email')
        ob.u_name = request.POST.get('uname')
        ob.contact = request.POST.get('ct')
        ob.password = request.POST.get('pwd')
        ob.location = request.POST.get('loc')
        ob.save()


    return render(request,'shop/Shop.html')

def viewshop(request):
    ob = Shop.objects.all()
    context = {
        'obval':ob,
    }
    return render(request,'shop/view_shop.html',context)

def approve2(request,idd):
    ob = Shop.objects.get(s_id=idd)
    ob.status="approved"
    ob.save()
    obj = Login()
    obj.username = ob.u_name
    obj.password = ob.password
    obj.type = "shop"
    obj.u_id = ob.s_id
    obj.save()
    return mngshop(request)

def reject(request,idd):
    ob = Shop.objects.get(s_id=idd)
    ob.status = "rejected"
    ob.save()
    return mngshop(request)

def searchshop(request):
    if request.method == "POST":
        a = request.POST.get('psch')
        obj = Shop.objects.filter(location__icontains=a)
        context={
            'obval':obj,
        }
        return render(request, 'shop/search_shop.html',context)

    return render(request,'shop/search_shop.html')



def mngshop(request):
    ob = Shop.objects.all()
    context ={
        'obval':ob,
    }
    return render(request,'shop/manage_shop.html',context)


def updat(request,idd):
    obj = Shop.objects.filter(s_id=idd)
    context={
        'obval':obj,
    }
    ob = Shop.objects.get(s_id=idd)
    if request.method=="POST":
        ob.s_name = request.POST.get('sname')
        ob.email = request.POST.get('Email')
        ob.u_name = request.POST.get('uname')
        ob.contact = request.POST.get('ct')
        ob.password = request.POST.get('pwd')
        ob.location = request.POST.get('loc')
        ob.save()
        return mngshop(request)



    return render(request, 'shop/update.html', context)

def deleteshop(request,idd):
    ob = Shop.objects.get(s_id=idd).delete()
    return mngshop(request)


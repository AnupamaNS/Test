from django.shortcuts import render
from product.models import Product
from category.models import Category

# Create your views here.
def prodreg(request):
    object = Category.objects.all()
    con={
        'aa':object
    }
    if request.method=="POST":
        ob = Product()
        ob.p_name = request.POST.get('prod')
        ob.price = request.POST.get('pri')
        ob.qty = request.POST.get('qty')
        ob.c_id = request.POST.get('cat')
        ob.s_id='1'
        ob.save()
    return render(request,'product/Product.html',con)

def viewprod(request):
    ob = Product.objects.all()
    context = {
        'obval':ob,
    }
    return render(request,'product/view_products.html',context)

def approve(request,idd):
    ob = Product.objects.get(p_id=idd)
    ob.status="approved"
    ob.save()
    return viewprod(request)

def reject(request,idd):
    ob = Product.objects.get(p_id=idd)
    ob.status="rejected"
    ob.save()
    return viewprod(request)

def searchprod(request):
    if request.method == "POST":
        a = request.POST.get('prsch')
        obj = Product.objects.filter(p_name__icontains=a)
        context ={
            'obval':obj,
        }
        return render(request,'product/search_prduct.html',context)
    return render(request,'product/search_prduct.html')


def mngprod(request):
    ob = Product.objects.all()
    context ={
        'obval':ob,
    }
    return render(request,'product/manage_product.html',context)

def update(request,idd):
    ob = Product.objects.filter(p_id=idd)
    context={
        'obva':ob,
    }
    if request.method=="POST":
        ob = Product.objects.get(p_id=idd)
        ob.p_name = request.POST.get('prod')
        ob.price = request.POST.get('pri')
        ob.qty = request.POST.get('qty')
        ob.c_id = request.POST.get('cat')
        ob.s_id=1
        ob.save()
        return mngprod(request)
    return render(request,'product/update.html',context)

def delete(request,idd):
    ob = Product.objects.get(p_id=idd).delete()
    return mngprod(request)

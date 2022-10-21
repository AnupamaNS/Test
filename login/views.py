from django.shortcuts import render
from login.models import Login

# Create your views here.
def login(request):
    if request.method == "POST":
        uname = request.POST.get("uname")
        passw = request.POST.get("pass")

        obj = Login.objects.filter(username=uname, password=passw)
        tp = ""
        for ob in obj:
            tp = ob.type
            uid = ob.u_id
            if tp == "admin":
                request.session["u_id"] = uid
                return render(request, 'temp/admin.html')
            elif tp == "shop":
                request.session["u_id"] = uid
                return render(request, 'temp/shop.html')
            elif tp == "user":
                request.session["u_id"] = uid
                return render(request, 'temp/user.html')
        #             # elif tp == "assistant":
        #             #     request.session["u_id"] = uid
        #             #     return render(request, 'temp/assistant.html')
        #             # else:
        objlist = "Username or Password incorrect... Please try again...!"
        context = {
            'msg': objlist,
        }
        return render(request, 'login/login.html', context)
    return render(request, "login/login.html")
    return render(request,'login/login.html')
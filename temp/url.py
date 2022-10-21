from django.conf.urls import url

from temp import views

urlpatterns=[
    url('main_home/',views.temp),
    url('admin/',views.admin),
    url('shop/',views.shop),
    url('user/',views.user),
]
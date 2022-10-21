from django.conf.urls import url
from product import views

urlpatterns=[
    url('prodreg/', views.prodreg),
    url('viewprod/', views.viewprod),
    url('mngprod',views.mngprod),
    url('approve/(?P<idd>\w+)', views.approve, name="approve"),
    url('reject/(?P<idd>\w+)', views.reject, name="reject"),
    url('update/(?P<idd>\w+)', views.update,name="update"),
    url('delete/(?P<idd>\w+)', views.delete, name="delete"),
    url('search/',views.searchprod),
]
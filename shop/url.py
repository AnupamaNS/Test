from django.conf.urls import url
from shop import views

urlpatterns=[
    url(r'^shopreg/', views.shopreg),
    url(r'^viewshop/', views.viewshop),
    url(r'^mngshop/', views.mngshop),
    url(r'^approve/(?P<idd>\w+)', views.approve2, name="approve1"),
    url(r'^reject/(?P<idd>\w+)', views.reject, name="reject"),
    url(r'^upd/(?P<idd>\w+)', views.updat, name="upd"),
    url(r'^delete/(?P<idd>\w+)', views.deleteshop, name="deleteshop"),
    url(r'^search/',views.searchshop),
]
from django.conf.urls import url
from complaint import views

urlpatterns=[
    url('cmpreg/', views.cmpreg),
    url('viewcmp/', views.viewcmp),
    url('reply/(?P<idd>\w+)', views.reply, name='replay'),
    url('viewrep/',views.viewrply)
]

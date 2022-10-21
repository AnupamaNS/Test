from django.conf.urls import url
from mask_violation import views

urlpatterns=[
    url('viewmask/', views.viewmask),
]
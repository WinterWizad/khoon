from django.urls import path
from . import views

app_name="newapp"

urlpatterns=[
    path('',views.index),
    path('home/',views.index,name="home"),
    path('emergency/',views.emergency, name="posts"),
    path('emergency/<slug:slug>',views.post_page, name="page"),
    path('submission/',views.submission, name="submission"),
    path('dlt_patient/<int:id>/',views.dlt_std),
    path('donor_list/',views.donor_list,name="donor_list")

]

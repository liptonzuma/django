from django.urls import path 
from . import views

urlpatterns =[
    path('',views.myfunctioncall,name='index'),
    path('bootstrap',views.bootstrap, name='bootstrap')

]
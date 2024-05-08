from . import views
from django.urls import path

urlpatterns = [
 
    path('',views.home,name='home'),
    path('conect',views.conect,name='conect'),
  
    path('<slug:slug>/',views.detalcar,name='detalcars'),
  
]

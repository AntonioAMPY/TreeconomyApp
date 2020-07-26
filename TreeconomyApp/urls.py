from django.urls import path
from . import views

app_name = 'App'

urlpatterns = [
    path('',views.getResponseProducts,name='index'),
    path('postResponseProducts/',views.postResponseProducts,name='postResponseProducts'),
    path('putProducts/',views.putProducts,name='putProducts'),
    path('deleteProducts/',views.deleteProducts,name='deleteProducts'),
]

from django.urls import path
from app import views

urlpatterns = [
    path('',views.index,name='index'),
    path('abour',views.about,name='about'),
    path('insert',views.insertData,name='insertData'),
]
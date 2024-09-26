from django.urls import path
from .import views

urlpatterns =[ 
    path('pix/',views.pixView,name='pix')

]

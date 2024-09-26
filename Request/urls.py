from django.urls import path
from .import views

urlpatterns =[
        path('trade4me/', views.trade4me_view, name='trade4me'),
        path('training/',views.training_view, name='training')
]

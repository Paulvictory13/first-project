from django.urls import path
from .import views

urlpatterns =[ 
        path('',views.home_view, name='home'),
        path('register',views.register_view, name='register'),
        path('login_ur/',views.login_view, name='login_ur'),
        path('logout/', views.logout_view, name='logout'),
        
#/////////////////  RETRIEVE  ///////////////////////////////////////////////////////////////////////////////////

        path('forget_password/',views.password_forget_view, name='forget_password'),
        path('password_reset/<str:reset_id>/',views.password_reset_view, name='password_reset'),
        path('password_reset_sent/<str:reset_id>/',views.password_reset_sent_view, name='password_reset_sent'),

#///////////////////////////////////////////////////////////////////////////////////////////////////////////////


]

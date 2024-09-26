from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.core.mail import EmailMessage
from django.utils import timezone
from django.urls import reverse
from .models import *
from .forms import *


# Create your views here.
#@login_required
"""
def trade4me_view(request):
    form = Trade4meForm()
    if request.method == 'POST':
        form = Trade4meForm(request.POST)
        if form.is_valid():
            form.save()
            full_name = request.POST.get('full_name')
            email = request.POST.get('email')   
            login_ID = request.POST.get('login_ID')   
            password = request.POST.get('password') 
            messages.success(request, 'We have receievd your request, a mail has been sent to you')
            return redirect('home')
        context = {'form':form}
    return render(request,'trade4me.html')
"""

#anytime class is assigned to a variable, its called object of the class or instance
@login_required
def trade4me_view(request):
    form = Trade4meForm()
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')   
        login_ID = request.POST.get('login_ID')   
        password = request.POST.get('password') 
        user = Trade4me.objects.create(full_name=full_name, 
                email = email, 
                login_ID=login_ID, 
                password=password
                )
        user.save()
        messages.success(request, 'We have receievd your request, a mail has been sent to you')
        return redirect('home')
    context = {'form':form}
    return render(request,'trade4me.html',context)











@login_required
def training_view(request):

    return render(request, 'training.html')

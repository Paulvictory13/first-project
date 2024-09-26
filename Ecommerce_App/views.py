from django.shortcuts import * 
from .models import *
from .forms import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required



@login_required
def pixView(request):
    return render(request,'pictures_page.html')

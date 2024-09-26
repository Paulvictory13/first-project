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
# from .forms import *


# Create your views here.

@login_required
def home_view(request):
    
    return render(request,'page_home.html')


def register_view(request):
    if request.method == 'POST':
        first_name = request.POST.get('First_name')
        last_name = request.POST.get('Last_name') 
        email = request.POST.get('email')   
        username = request.POST.get('username')   
        password = request.POST.get('password')   

        user_data_has_error = False

        if User.objects.filter(username=username).exists():
            user_data_has_error = True
            messages.error(request,"username already exist")

        if User.objects.filter(email=email).exists():
            user_data_has_error = True
            messages.error(request,"email already exist")

        if len(password) < 7:
            user_data_has_error = True
            messages.error(request,"password must be at least 7 characters")

        if user_data_has_error:
            return redirect('register')
        else:
            User.objects.create_user(
                first_name=first_name,
                last_name=last_name,
                email=email,
                username=username,
                password=password )
            messages.success(request, "Account created, login now")
            return redirect('login_ur')
    return render(request,'page_register.html')


#//////////////////////////////////////////////////////////////////////////////////////////////////////////////


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
        
            return redirect('home')
        
        else:
            messages.error(request, "invalid login details")
            return redirect('login_ur')
    return render(request,'page_login.html')

def logout_view(request):
    logout(request)
    return redirect('login_ur')

#//////////////////////////////////////////////////////////////////////////////////////////////////////////


def password_forget_view(request):
    if request.method == "POST":
        email = request.POST.get('email')
        print(email, 'user email')
        try:
            user = User.objects.get(email=email)
            new_password_reset = Password_Reset(user=user)
            new_password_reset.save()

            password_reset_url = reverse('password_reset',kwargs={'reset_id': new_password_reset.reset_id})
            print(password_reset_url, 'Print password reset url')
            full_password_reset_url = f'{request.get_scheme}://{request.get_host()}{password_reset_url}'
            email_body = f'Reset your password using the link below:\n\n\n{full_password_reset_url}',
        
            email_message = EmailMessage(
                'Reset your password',      #email subject
                email_body,
                settings.EMAIL_HOST_USER,   # for sender
                [email]    #for receiver 
            )

            email_message.fail_silently = True
            email_message.send()

            return redirect('password_reset_sent', reset_id=new_password_reset.reset_id)

        except User.DoesNotExist:
            messages.error(request, f"No user with email '{email}' found")
            return redirect('forget_password')
    return render(request,'password_forget.html')

def password_reset_sent_view(request, reset_id):
    
    if Password_Reset.objects.filter(reset_id).exists():
        return render(request, 'password_reset_sent.html')
    else:
        messages.error(request,'Invalid reset id')
        return redirect('password_forget')


def password_reset_view(request, reset_id):
    try:
        password_reset_id = Password_Reset.objects.get(reset_id=reset_id)

        if request.method == "POST":
            password = request.POST.get('password')
            confirm_password = request.POST.get('confirm_password')

            passwords_have_error = False

            if password != confirm_password:
                passwords_have_error = True
                messages.error(request, 'Password do not match')

        if len(password) < 5:
            passwords_have_error = True
            messages.error(request, 'Password must be at least 5 characters long')

        expiration_time = password_reset_id.created_when + timezone.timedelta(minutes=10)

        if timezone.now() > expiration_time:
            passwords_have_error =  True
            messages.error(request, 'Reset link has expired')

            reset_id.delete()

        if not passwords_have_error:
            user = password_reset_id.user
            user.set_password(password)
            user.save()

            reset_id.delet()

            messages.success(request, 'Password reset. Proceed to login')
            return redirect('login_ur')
        else:
            return redirect('password_reset', reset_id=reset_id)

    except Password_Reset.DoesNotExist:

        messages.error(request,'Invalid reset id')
        return redirect('password_forget')
    #return render(request,'password_reset_sent.html')

    

    #return render(request,'password_reset.html')

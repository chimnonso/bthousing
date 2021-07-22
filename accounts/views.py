from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.add_message(request, messages.SUCCESS, 'Login Successful')
            return redirect('index')
        else:
            messages.add_message(request, messages.ERROR, 'Invalid Credentials. Login Unsuccessful')
            return redirect('login')
    
    return render(request, 'accounts/login.html')


def register(request):
    is_correct = True
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        
        if password == password2:
            
            if User.objects.filter(username=username).exists():
                messages.add_message(request, messages.ERROR, 'Username already exists')
                return redirect('register')

            else:
                if User.objects.filter(email=email).exists():
                    messages.add_message(request, messages.ERROR, 'Email already exists')
                    return redirect('register')
        
                else:
                    user = User.objects.create_user(
                        username=username, last_name=last_name, first_name=first_name, email=email, password=password
                    )
                    # auth.login(request, user)
                    messages.add_message(request, messages.SUCCESS, 'Thanks for registering. Login Below')

                    return redirect('login')

        else:
            messages.add_message(request, messages.ERROR, 'Passwords must match')
            return redirect('register')

    context = {}
    return render(request, 'accounts/register.html', context)


def dashboard(request):
    
    context = {}
    return render(request, 'accounts/dashboard.html', context)

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.add_message(request, messages.SUCCESS, 'Logged out successfully')
        return redirect('index')
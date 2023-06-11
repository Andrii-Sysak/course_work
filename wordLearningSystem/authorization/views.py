from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# from main.models import Registration, Login
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Users
from dictionary.models import Personaldict


# Create your views here.
def register(request):
    form = UserCreationForm()
    error = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            password = form.cleaned_data.get('password1')
            password2 = form.cleaned_data.get('password2')
            if password != password2:
                form.add_error('password2', "Passwords do not match")
                error = 'Паролі не співпадають'
            else:
                form.save()
                username = form.cleaned_data.get('username')
                new_email = username + '@email.com'
                user = Users(
                    email=new_email,
                    password=password,
                    name=username,
                )
                user.save()

                personal_dict = Personaldict(user=user)
                personal_dict.save()

                return redirect('/account/login')
        else:
            error = 'Введені неправильні дані'
    else:
        form = UserCreationForm()
    data = {
        'form': form,
        'error' : error,
    }
    return render(request, 'authorization/register.html', data)



def logIn(request):
    error = ''
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username,password=password)
        if user:
            if user.is_active:
                login(request,user)
                return redirect('/')
        else:
            error = 'Логін або пароль введено неправильно'
    else:
        form = AuthenticationForm()
    data = {
        'form' : form,
        'error': error,
    }
    return render(request,'authorization/login.html', data)

# def logined(username):
#     date_time = datetime.datetime.now()
#     obj = Login(username=username, login_date=date_time)
#     obj.save()


def logOut(request):
    logout(request)
    return redirect('/account/login')



from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, get_user_model, login
from django.contrib.auth.decorators import login_required
from account.forms import LoginForm
from django.contrib.auth.models import User
from account.views import dashboard

# Create your views here.

def landing(request):
    if request.user.is_authenticated:
        return redirect('account/dashboard')

    form = LoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('/')
            else:
                form.add_error('username', 'اکانت موردنظر غیرفعال شده است')
        else:
            form.add_error('username', f"کاربری با مشخصات وارد شده یافت نشد! \n" + " نام کاربری یا رمز عبور اشتباه است!")
    context = {
        'form': form
    }
    return render(request, 'account/login.html', context)
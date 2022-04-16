from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, get_user_model, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import LoginForm, UserRegistrationForm, UserEditForm, ProfileEditForm
from .models import Profile
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from common.decorators import ajax_required
from .models import Contact
from actions.utils import create_action
from actions.models import Action


# Create your views here.
def user_login(request):
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
 



@login_required()  
def dashboard(request):
    # Display all actions by default
    actions = Action.objects.exclude(user=request.user)
    following_ids = request.user.following.values_list('id', flat=True)
    if following_ids:
        # If user is following others, retrieve only their actions
        actions = actions.filter(user_id__in=following_ids)
    actions = actions.select_related('user', 'user__profile')\
        .prefetch_related('target')[:10]
    
    return render(request, 'account/dashboard.html', {'section':'dashboard', 'actions':actions})


      
    
def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            Profile.objects.create(user=new_user)
            create_action(new_user, 'یک اکانت در وینکی ساخت.')
            return render(request, 'account/register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
        context = {
            'user_form': user_form
        }    
    return render(request, 'account/register.html', context)
                     


@login_required
def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile, data=request.POST, files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            #messages.add_message(request, messages.SUCCESS, "پروفایل شما با موفقیت ویرایش شد!")
            messages.success(request, "پروفایل شما با موفقیت ویرایش شد!")
        else:
            messages.error(request, "ویرایش پروفایل انجام نشد!")
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
    return render(request, 'account/edit.html', {'user_form': user_form, 'profile_form': profile_form})
    
    
@login_required
def user_list(request):
    users = User.objects.filter(is_active=True)
    return render(request, 'account/user/list.html', {'section': 'people', 'users': users})


@login_required
def user_detail(request, username):
    user = get_object_or_404(User, username=username, is_active=True)
    return render(request, 'account/user/detail.html', {'section': 'people', 'user': user})    
    
    
@ajax_required
@require_POST
@login_required
def user_follow(request):
    user_id = request.POST.get('id')
    action = request.POST.get('action')
    if user_id and action:
        try:
            user = User.objects.get(id=user_id)
            if action == 'follow':
                Contact.objects.get_or_create(user_from=request.user, user_to=user)
                create_action(request.user, 'فالو می کند', user)
            else:
                Contact.objects.filter(user_from=request.user, user_to=user).delete()
            return JsonResponse({'status':'ok'})
        except User.DoesNotExist:
            return JsonResponse({'status':'error'})
    return JsonResponse({'status':'error'})
    
    
    
    
    
    
    
    
    


#def user_login(request):
 #   if request.method == 'POST':
  #      form = LoginForm(request.POST)
   #     if form.is_valid():
    #        cd = form.cleaned_data
     #       user = authenticate(request,
      #                          username=cd['username'],
       #                         password=cd['password'])
        #    if user is not None:
         #       if user.is_active:
          #          login(request, user)
           #         return HttpResponse('Authenticated '\
            #                            'successfully')
             #   else:
              #      return HttpResponse('Disabled account')
            #else:
             #   return HttpResponse('Invalid login')
    #else:
     #   form = LoginForm()
    #return render(request, 'account/login.html', {'form': form}) 


#def register(request):
 #   if request.user.is_authenticated:
  #      return redirect('/')
   # register_form = RegisterForm(request.POST or None)
#
 #   if register_form.is_valid():
  #      first_name = register_form.cleaned_data.get('first_name')
   #     last_name = register_form.cleaned_data.get('last_name')
    #    user_name = register_form.cleaned_data.get('user_name')
     #   password = register_form.cleaned_data.get('password')
      #  gender = register_form.cleaned_data.get('gender')
       # email = register_form.cleaned_data.get('email')
        #User.objects.create_user(first_name=first_name, last_name=last_name, username=user_name, email=email, password=password)
        
        #return redirect('/login')

    #context = {
     #   'register_form': register_form
    #}
    #return render(request, 'account/register.html', context)
    
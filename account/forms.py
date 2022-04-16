from django import forms
from django.contrib.auth.models import User
from django.forms.fields import DateField, ChoiceField, MultipleChoiceField
from django.forms.widgets import RadioSelect, CheckboxSelectMultiple
from django.core import validators
from .models import Profile


messages = {
	'required':'این فیلد اجباری است',
	'invalid':'لطفا یک ایمیل معتبر وارد کنید',
	'max_length':'تعداد کاراکترها بیشتر از حد مجاز است'
}

        
class LoginForm(forms.Form):
    username = forms.CharField(error_messages=messages, max_length=30, label='نام کاربری', widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(error_messages=messages, max_length=40, label='گذرواژه', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    

GENDER_CHOICES = (('m', 'مرد'), ('f', 'زن'), ('u', 'ترجیح می دهم نگویم'))
class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(max_length=40, widget=forms.PasswordInput(attrs={'class':'form-control'}), label='گذرواژه')
    password2 = forms.CharField(max_length=40, widget=forms.PasswordInput(attrs={'class':'form-control'}), label='تکرار گذرواژه')
    gender = ChoiceField(widget=RadioSelect, label='جنسیت', choices=GENDER_CHOICES)
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')
    
    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('رمز عبور و تکرار رمز عبور یکسان نیستند')
        return cd['password2']
        



class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

        
        
class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('date_of_birth', 'photo')
        
        
        



#class LoginForm(forms.Form):
 #   user_name = forms.CharField(
 #       widget=forms.TextInput,
 #       label='نام کاربری'
 #   )

 #   password = forms.CharField(
 #       widget=forms.PasswordInput,
 #      label='کلمه ی عبور'
 #   )

 #   def clean_user_name(self):
 #       user_name = self.cleaned_data.get('user_name')
 #       is_exists_user = User.objects.filter(username=user_name).exists()
 #       if not is_exists_user:
 #           raise forms.ValidationError('کاربری با مشخصات وارد شده ثبت نام نکرده است')

#        return user_name
        
        
        
        
#GENDER_CHOICES = (('m', 'مرد'), ('f', 'زن'), ('u', 'ترجیح می دهم نگویم'))

#class RegisterForm(forms.Form):
#    first_name = forms.CharField(
#        widget=forms.TextInput,
#        label='نام',
#        validators=[
#            validators.MaxLengthValidator(limit_value=20,
#                                          message='تعداد کاراکترهای وارد شده نمیتواند بیشتر از 20 باشد'),
#           validators.MinLengthValidator(8, 'تعداد کاراکترهای وارد شده نمیتواند کمتر از 8 باشد')
#        ]
#    )
    
#    last_name = forms.CharField(
#        widget=forms.TextInput,
#        label='نام خانوادگی',
#        validators=[
#            validators.MaxLengthValidator(limit_value=20,
#                                          message='تعداد کاراکترهای وارد شده نمیتواند بیشتر از 20 باشد'),
#            validators.MinLengthValidator(8, 'تعداد کاراکترهای وارد شده نمیتواند کمتر از 8 باشد')
#        ]
#    )
    
#    user_name = forms.CharField(
#        widget=forms.TextInput,
#        label='نام کاربری',
#        validators=[
#            validators.MaxLengthValidator(limit_value=20,
 #                                         message='تعداد کاراکترهای وارد شده نمیتواند بیشتر از 20 باشد'),
  #          validators.MinLengthValidator(8, 'تعداد کاراکترهای وارد شده نمیتواند کمتر از 8 باشد')
   #     ]
    #)
    
#    gender = ChoiceField(
#        widget=RadioSelect,
#        label='جنسیت',
#        choices=GENDER_CHOICES
#    )
    
#    email = forms.CharField(
#        widget=forms.TextInput(attrs={'placeholder': 'لطفا ایمیل خود را وارد نمایید'}),
 #       label='ایمیل',
  #      validators=[
   #         validators.EmailValidator('ایمیل وارد شده معتبر نمیباشد')
    #    ]
    #)

#    password = forms.CharField(
#        widget=forms.PasswordInput,
#        label='کلمه ی عبور'
#    )

#    re_password = forms.CharField(
 #       widget=forms.PasswordInput,
  #      label='تکرار کلمه ی عبور'
   # )

#    def clean_email(self):
 #       email = self.cleaned_data.get('email')
  #      is_exists_user_by_email = User.objects.filter(email=email).exists()
   #     if is_exists_user_by_email:
    #        raise forms.ValidationError('ایمیل وارد شده تکراری میباشد')

      #  if len(email) > 20:
     #       raise forms.ValidationError('تعداد کاراکترهای ایمیل باید کمتر از 20 باشد')

       # return email

   # def clean_user_name(self):
     #   user_name = self.cleaned_data.get('user_name')
    #    is_exists_user_by_username = User.objects.filter(username=user_name).exists()

      #  if is_exists_user_by_username:
       #     raise forms.ValidationError('این کاربر قبلا ثبت نام کرده است')

        #return user_name

   # def clean_re_password(self):
    #    password = self.cleaned_data.get('password')
     #   re_password = self.cleaned_data.get('re_password')
      #  print(password)
       # print(re_password)

        #if password != re_password:
         #   raise forms.ValidationError('کلمه های عبور مغایرت دارند')

        #return password
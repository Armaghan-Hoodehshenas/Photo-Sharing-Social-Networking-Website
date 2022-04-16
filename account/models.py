from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='کاربر')
    date_of_birth = models.DateField(blank=True, null=True, verbose_name='تاریخ تولد')
    photo = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True, verbose_name='عکس پروفایل')
    
    def __str__(self):
        return f'Profile for user {self.user.username}'
        
    class Meta:
        verbose_name = 'پروفایل'
        verbose_name_plural = 'پروفایلها'
        
        
class Contact(models.Model):
    user_from = models.ForeignKey('auth.User', related_name='rel_from_set', on_delete=models.CASCADE, verbose_name='فالو کننده')
    user_to = models.ForeignKey('auth.User', related_name='rel_to_set', on_delete=models.CASCADE, verbose_name='فالو شونده')
    created = models.DateTimeField(auto_now_add=True, db_index=True)
    
    class Meta:
        ordering = ('-created',)
        verbose_name = 'فالو کردن'
        verbose_name_plural = 'فالو کردن ها'
        
    def __str__(self):
        return f'{self.user_from} {self.user_to} فالو می کند'
        
# Add following field to User dynamically
user_model = get_user_model()
user_model.add_to_class('following', models.ManyToManyField('self', through=Contact, related_name='followers', symmetrical=False))
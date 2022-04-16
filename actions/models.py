from django.db import models
###from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

# Create your models here.

class Action(models.Model):
    ###user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='image_created', on_delete=models.CASCADE, verbose_name='کاربر')
    user = models.ForeignKey('auth.User', related_name='actions', db_index=True, on_delete=models.CASCADE, verbose_name='کاربر')
    verb = models.CharField(max_length=255, verbose_name='رخداد')
    created = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='تاریخ رخداد')
    target_ct = models.ForeignKey(ContentType, blank=True, null=True, related_name='target_obj', on_delete=models.CASCADE, verbose_name='آبجکت هدف')
    target_id = models.PositiveIntegerField(null=True, blank=True, db_index=True, verbose_name='آی دی هدف')
    target = GenericForeignKey('target_ct', 'target_id')
    
    target.short_description = ('هدف')
    
    class Meta:
        ordering = ('-created',)
        verbose_name = 'رخداد'
        verbose_name_plural= 'رخدادها'
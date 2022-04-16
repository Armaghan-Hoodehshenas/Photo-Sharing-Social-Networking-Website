from django.db import models
from django.conf import settings
from django.utils.text import slugify
from django.urls import reverse

# Create your models here.
class Image(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='image_created', on_delete=models.CASCADE, verbose_name='کاربر')
    title = models.CharField(max_length=200, verbose_name='عنوان')
    slug = models.SlugField(max_length=200, blank=True, null=True, verbose_name='اسلاگ')
    url = models.URLField(null=True)
    image = models.ImageField(upload_to='images/%y/%m/%d/', verbose_name='عکس')
    description = models.TextField(blank=True, verbose_name='کپشن')
    created = models.DateField(auto_now_add=True, db_index=True, verbose_name='تاریخ ایجاد مطلب')
    users_like = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='images_liked', blank=True, verbose_name='تعداد لایک ها')
    total_likes = models.PositiveIntegerField(db_index=True, default=0)
    
    def __str__(self):
        return self.title
        
        
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.url) #self.title
        super().save(*args, **kwargs)
        
    class Meta:
        verbose_name = 'عکس'
        verbose_name_plural= 'عکس ها'
        
    def get_absolute_url(self):
        return reverse('images:detail', args=[self.id, self.slug]) 
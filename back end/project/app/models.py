from django.db import models
import os
from django.utils.text import slugify
from django_ckeditor_5.fields import CKEditor5Field
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.

def image_upload(instance, filename):
    name, extension = os.path.splitext(filename)
    return f"pro/{instance.id}{extension}"

class Product(models.Model):
    title = models.CharField(max_length=50 , verbose_name='إسم المنتج:')
    price = models.IntegerField(verbose_name="السعر")
    img1 = models.ImageField(upload_to=image_upload, verbose_name="الصورة الرئيسية")
    img2 = models.ImageField(upload_to=image_upload, verbose_name="الصورة2", null=True, blank=True)
    img3 = models.ImageField(upload_to=image_upload, verbose_name="الصورة3", null=True, blank=True)
    # quantity = models.IntegerField(verbose_name="الكمية")
    details = CKEditor5Field(blank=True, null=True, verbose_name="الوصف", config_name='extends')
    active = models.BooleanField(default=True)
    slug = models.SlugField(null=True, blank=True)


    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Product, self).save(*args, **kwargs)
    

    def __str__(self):
        return self.title
    


def image_upload_cat(instance, filename):
    name, extension = os.path.splitext(filename)
    return f"cat/{instance.id}{extension}"
    
class Blog(models.Model):
    name = models.CharField(max_length=50 , verbose_name='إسم المقال:')
    author = models.CharField(max_length=50 , verbose_name='إسم الكاتب:')
    img = models.ImageField(upload_to=image_upload_cat, verbose_name="الصورة:")
    details = CKEditor5Field(blank=True, null=True, verbose_name="الوصف", config_name='extends')
    published_at = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    slug = models.SlugField(null=True, blank=True)



    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Blog, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
    

# ORDERS
class Order(models.Model):
    STATUS_CHOICES = [
        ('delivered', 'تم التسليم'),
        ('confirmed', 'تم التأكيد'),
        ('canceled', 'ملغي'),
        ('in_progress', 'جاري التوصيل'),
        ('changed', 'تم تغيير الطلبية'),
    ]

    DELIVERY_CHOICES = [
        ('stop_desk', 'المكتب'),
        ('home', 'المنزل'),
    ]
    STATE_CHOICES = [
        ('الشلف', 'الشلف'),
        ('الجزائر', 'الجزائر'),
        ('عين الدفلى', 'عين الدفلى'),
    ]
    product = models.ForeignKey(Product, related_name='apply_order', verbose_name="إسم المنتج", on_delete=models.CASCADE)
    name = models.CharField(max_length=50, verbose_name="إسمك الكامل")
    phone = models.IntegerField(verbose_name="رقم الهاتف")
    state = models.CharField(max_length=50, choices=STATE_CHOICES, verbose_name="الولاية")
    city = models.CharField(max_length=50, verbose_name="البلدية")
    order_at = models.DateTimeField(auto_now=True, verbose_name="وقت نشر الطلبية")
    quantity = models.IntegerField(verbose_name="الكمية", null=True, blank=True, default=1, validators=[MinValueValidator(1), MaxValueValidator(100)])
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, null=True, blank=True, verbose_name="الحالة")
    delivery = models.CharField(max_length=50, choices=DELIVERY_CHOICES, null=True, blank=True, verbose_name="نوع التوصيل")

    def __str__(self):
        return self.name
from django.shortcuts import render , redirect , HttpResponse
from .models import *
from .form import *
# Create your views here.

def home(request):
    pro = Product.objects.all()
    blog = Blog.objects.all()
    context={
        'pro':pro,
        'blog':blog
    }
    return render(request , 'pages/index.html' ,context)

def products(request):
    pro = Product.objects.all()
    blog = Blog.objects.all()
    context={
        'pro':pro,
        'blog':blog
    }
    return render(request , 'pages/products.html' ,context)


def details(request, slug):
    detail = Product.objects.get(slug=slug)
    # تعيين قيمة افتراضية لـ pro_list
    pro_list = None

    if request.method == 'POST':
        form = OrderForm(request.POST, request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.product = detail
            myform.save()
            return redirect('stor:index')  # Redirect to the index page after successful form submission
    else:
        form = OrderForm()
        # تعيين قيمة لـ pro_list في الحالة الأخيرة
        pro_list = Product.objects.all()

    context = {
        'det': detail,
        'form': form,
        'pro': pro_list,
    }
    return render(request, 'pages/pro-details.html', context)

def blogs(request):
    blogs = Blog.objects.all()
    context={
        'blog':blogs
    }
    return render(request , 'pages/blogs.html' ,context)


def blog(request, slug):
    detail = Blog.objects.get(slug=slug)
    context = {
        'det': detail,
    }
    return render(request, 'pages/sigle-blog.html', context)


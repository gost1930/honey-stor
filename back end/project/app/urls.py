from django.urls import path , include
from . import views
app_name='app'
urlpatterns = [
    path('', views.home , name='home'),
    path('products/', views.products , name='products'),

    path('<str:slug>', views.details, name='details'),

    path('blogs/', views.blogs , name='blogs'),

    path('blogs/<str:slug>', views.blog, name='blog'),

]
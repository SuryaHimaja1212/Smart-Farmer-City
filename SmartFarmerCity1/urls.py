"""
URL configuration for SmartFarmerCity1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('cust_register/', views.cust_register, name='cust_register'),
    path('login/', views.login, name='login'),
    path('cust_login/', views.cust_login, name='cust_login'),
    path('customer/',views.customer,name='customer'),
    path('farmer/', views.farmer, name='farmer'),
    path('farmer/add/', views.add, name='add'),
    path('farmer/add/add.html/', views.farmer, name='farmer'),
    path('farmer/remove/', views.remove, name='remove'),
    path('farmer/update/', views.update, name='update'),
    path('farmer/view/', views.view, name='view'),
    path('customer/cust_login.html',views.cust_login,name='cust_login'),
]
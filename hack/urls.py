"""hack URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from app1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Home, name="homepage"),
    path('donate/', views.donate, name="donate"),
    path('donate_ut/', views.donate_ut, name="donate_ut"),
    path('donate_form/', views.donate_form, name="donate_form"),
    path('payment/', views.payment, name="payment"),
    path('thanks/', views.thanks, name="thanks"),
    path('report/', views.report, name="report"),
    path('about/', views.about, name="about")
]

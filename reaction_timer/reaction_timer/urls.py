"""reaction_timer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from main.views import *

urlpatterns = [
    path('', registration, name='registration'),
   
    path('experiment1/<str:username>', first_experiment, name='first_experiment'),
    path('experiment2/<str:username>', second_experiment, name='second_experiment'),
    path('experiment3/<str:username>', third_experiment, name='third_experiment'),
    path('experiment4/<str:username>', fourth_experiment, name='fourth_experiment'),
    path('results', results, name='results'),
    path('admin/', admin.site.urls),
]


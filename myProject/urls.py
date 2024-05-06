"""
URL configuration for myProject project.

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
from Recipe import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name="home"),
    path('recipe_details/',views.recipe_details,name="recipe_details"),
    path('breakfast_recipe/',views.breakfast_recipe, name="breakfast_recipe"),
    path('dinner_recipe/',views.dinner_recipe, name="dinner_recipe"),
    path('juice_recipe/',views.juice_recipe, name="juice_recipe"),
    path('lunch_recipe/',views.lunch_recipe, name="lunch_recipe"),
    path('sweet_recipe/',views.sweet_recipe, name="sweet_recipe"),
    path('breakfast/<int:id>/', views.breakfast_detail, name='breakfast_detail'),
    path('dinner/<int:id>/', views.dinner_detail, name='dinner_detail'),
    path('juice/<int:id>/', views.juice_detail, name='juice_detail'),
    path('lunch/<int:id>/', views.lunch_detail, name='lunch_detail'),
    path('sweet/<int:id>/', views.sweet_detail, name='sweet_detail'),
]


if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

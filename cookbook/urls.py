"""
URL configuration for cookbook project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework.schemas import get_schema_view

from recipes.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/drf-auth/', include('rest_framework.urls')),
    path('swagger-ui/', TemplateView.as_view(
          template_name='swagger-ui.html',
          extra_context={'schema_url': 'openapi-schema'}
          ), name='swagger-ui'),

    # path('swagger-ui/', get_schema_view(
    #        title='Dish recipes',
    #        description='API for testing backend'),
    #        name='swagger-ui'),

    path('api/v1/dishlist/', DishAPIList.as_view()),
    path('api/v1/dishdetail/<int:pk>/', DishAPIDetailView.as_view()),
    path('api/v1/dishlist/category/<int:pk>/', DishCategoryAPIList.as_view()),
    path('api/v1/dishupdate/<int:pk>/', DishAPIUpdate.as_view()),
    path('api/v1/dishdelete/<int:pk>/', DishAPIDestroy.as_view()),
    path('', HomePageView.as_view(), name='home_page'),

]

"""CBV_REST_Company URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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

from testapp import views



urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.CompanyCRUDListView.as_view(), name="List"),
    path("detail/<int:pk>", views.ComaontCRUDDetailView.as_view(), name="detail"),
    path("create/", views.CompanyCRUDCreateView.as_view(), name="create"),
    path("update/<int:pk>", views.CompanyCRUDUpdateView.as_view(), name="update"),
    path("delete/<int:pk>", views.CompanyCRUDDeleteView.as_view(), name="Delete"),
    
    path("api/", include("testapp.api.urls")),

]

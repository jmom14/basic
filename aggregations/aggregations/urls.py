"""
URL configuration for aggregations project.

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
from django.urls import path, include
from examples import views

v1urls = [
    path("books/<int:pk>/rating", views.rate_book, name="rate_book"),
    path("books/<int:pk>", views.book_detail, name="book_detail"),
]

v2urls = [
    path("books/", include("examples.urls")),
]


urlpatterns = [
    path("admin/", admin.site.urls, name="admin"),
    path("api/v1/", include(v1urls)),
    path("api/v2/", include(v2urls)),
]

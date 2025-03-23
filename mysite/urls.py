from django.contrib import admin
from django.urls import path, include
from conventions import views 

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("accounts.urls")), 
    path("accounts/", include("django.contrib.auth.urls")),
    path("", views.home, name="home"),
    path('getting-started/', views.getting_started, name='gettingStarted'),
    path('<slug:slug>/', views.con_detail, name='con_detail'),
]


"""
# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('<slug:slug>/', views.artist_detail, name='artist_detail'),
]
"""
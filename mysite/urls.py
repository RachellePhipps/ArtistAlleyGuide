from django.contrib import admin
from django.urls import path, include
from conventions import views 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("accounts.urls")), 
    path("accounts/", include("django.contrib.auth.urls")),
    path("", views.home, name="home"),
    path('getting-started/', views.getting_started, name='gettingStarted'),
    path('search/', views.search_view, name='search'),
    path('<slug:slug>/', views.con_detail, name='con_detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


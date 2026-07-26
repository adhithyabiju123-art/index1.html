from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from tracker.views import dashboard, register, tracker

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),

    path('', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('register/', register, name='register'),
    path('tracker/', tracker, name='tracker'),
    path('dashboard/', dashboard, name='dashboard'),
]
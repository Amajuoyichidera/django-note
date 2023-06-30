from django.urls import path
from . import views
import django.contrib.auth.views as auth_views


app_name='notes'

urlpatterns = [
    path('', views.index, name='home'),
    path('login/', auth_views.LoginView.as_view(template_name='notes/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='notes/logged.html'), name='logout'),
    path('register/', views.register, name='register'),
    path('settings/', views.settings, name='settings'),
    path('update/', views.update, name='update'),
    path('home/', views.home_page, name='home_page'),
]
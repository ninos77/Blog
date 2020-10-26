from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.login_v, name='login_v'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout_v, name='logout_v')
]

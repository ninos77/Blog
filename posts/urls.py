from django.urls import path
from . import views


urlpatterns = [
    path('', views.post, name='post'),
    path('<int:id>', views.detail, name='detail'),
    path('create/', views.create, name='create'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('update/<int:id>', views.update, name='update'),

]

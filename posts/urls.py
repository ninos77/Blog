from django.urls import path
from . import views


urlpatterns = [
    path('post/', views.post, name='post'),
    path('detail/<int:id>', views.detail, name='detail')
]

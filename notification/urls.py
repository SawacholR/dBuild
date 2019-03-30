from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_notification, name='noti'),
    path('noti/<int:pk>', views.detail_notification, name='noti-detail'),
    path('noti/create', views.notification_creation, name='create-noti'),
    path('noti/gallery', views.show_picture, name='show-pic')
]
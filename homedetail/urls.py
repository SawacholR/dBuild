from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('data', views.view_data, name='data'),
    path('profile', views.view_profile, name='view-profile')
]


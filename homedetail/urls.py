from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('data', views.view_data, name='data'),
    path('data/<int:pk>', views.DataDetailView.as_view(), name='data-detail'),
    path('room', views.view_room, name='room'),
    path('room/<uuid:pk>', views.RoomDetailView.as_view(), name='room-detail'),
    path('room/<uuid:pk>/show-data', views.data_list, name='room-data'),
]


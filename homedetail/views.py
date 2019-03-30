from homedetail.models import Room, DataType, Data
from django.views import generic
from django.views.generic import TemplateView
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required


# Create your views here.


class RoomDetailView(generic.DetailView):
    model = Room


def view_room(request):
    user = request.user
    room = Room.objects.filter(UserID=user.id)
    return render(request, 'homedetail/room_list.html', {'room_list': room})


def data_list(request, pk, room_filter=None):
    data = Data.objects.filter(RoomId=pk)
    if room_filter:
        room_filter = get_object_or_404(Room)
        data = data.filter(RoomId=room_filter)
    return render(request, 'homedetail/data_in_the_room.html', {'data': data})


class DataDetailView(generic.DetailView):
    model = Data


class DataListView(generic.ListView):
    model = Data
    paginate_by = 10


@login_required
def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_rooms = Room.objects.all().count()

    # Available books (status = 'a')
    room_avilable = Room.objects.filter(status__exact='a').count()

    # The 'all()' is implied by default.
    num_datas = Data.objects.count()

    context = {
        'num_rooms': num_rooms,
        'room_avilable': room_avilable,
        'num_datas': num_datas,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

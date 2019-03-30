from django.shortcuts import render
from homedetail.models import Room
from notification.models import GlobalNotification
from .forms import CreateNotificationForm
# Create your views here.


def view_notification(request):
    global_notification = GlobalNotification.objects.all()
    return render(request, 'notification/notification_list.html', {'global': global_notification})


def detail_notification(request, pk):
    global_notification = GlobalNotification.objects.filter(id=pk)
    print(global_notification)
    return render(request, 'notification/notification_detail.html', {'global': global_notification})


def notification_creation(request):
    user = request.user
    if request.method == 'GET':
        form = CreateNotificationForm()
        return render(request, 'notification/create.html', {'form': form})
    if request.method == 'POST':
        form = CreateNotificationForm(request.POST, request.FILES)
        if form.is_valid():
            topic = form.cleaned_data['Topic']
            detail = form.cleaned_data['Detail']
            picture = form.cleaned_data['Picture']
            date = form.cleaned_data['Date']
            noti = GlobalNotification(Topic=topic,
                                      Detail=detail,
                                      Picture=picture,
                                      Date=date)
            noti.save()

            return render(request, 'notification/notification_detail.html', {'notification': noti})
        else:
            print(request.FILES)
            print(form.errors)
            return render(request, 'notification/create.html', {'form': form})

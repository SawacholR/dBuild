from django.shortcuts import render
from notification.models import GlobalNotification
from .forms import CreateNotificationForm
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
# Create your views here.


def show_picture(request):
    random_pic = GlobalNotification.objects.all()
    paginator = Paginator(random_pic, 2)
    page = request.GET.get('page')
    current = paginator.get_page(page)

    return render(request, 'notification/show-pic.html', {'global': random_pic,
                                                          'page': current})


def view_notification(request):
    global_notification = GlobalNotification.objects.all()
    return render(request, 'notification/notification_list.html', {'global': global_notification})


def detail_notification(request, pk):
    global_notification = GlobalNotification.objects.filter(id__exact=pk)
    print(global_notification)
    picture = global_notification.values('Picture').get()
    picture_path = picture['Picture']
    print(global_notification.values('Picture').get())
    print(picture_path)
    return render(request, 'notification/notification_detail.html', {'notification': global_notification,
                                                                     'picture_path': picture_path})


@login_required
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
            working = form.cleaned_data['Working_Hour']
            pay = form.cleaned_data['Pay']
            noti = GlobalNotification(Topic=topic,
                                      Detail=detail,
                                      Picture=picture,
                                      Date=date,
                                      Working_Hour=working,
                                      Pay=pay)
            noti.save()
            return render(request, 'notification/created.html', {'notification': noti})
        else:
            print(request.FILES)
            print(form.errors)
            return render(request, 'notification/create.html', {'form': form})

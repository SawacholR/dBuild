from django.contrib import admin
from notification.models import GlobalNotification
# Register your models here.


@admin.register(GlobalNotification)
class GlobalNotificationAdmin(admin.ModelAdmin):
    list_display = ('Topic', 'Detail', 'Created_date', 'Picture', 'Date')




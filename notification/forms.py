from django import forms
from .models import GlobalNotification
from django.contrib.auth.models import User


class CreateNotificationForm(forms.ModelForm):

    class Meta:
        model = GlobalNotification
        fields = ['Topic', 'Detail', 'Date', 'Picture']


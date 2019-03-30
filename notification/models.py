from django.db import models
from homedetail.models import Room, Data
from django.urls import reverse
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.


class GlobalNotification(models.Model):
    """Model representing a notification that aims to send to everyone"""
    Topic = models.CharField(max_length=200, help_text='Enter The Topic of the notification')
    Detail = models.TextField(max_length=1000, help_text='Enter a brief description of the notification')
    Created_date = models.DateTimeField(auto_now_add=True)
    Picture = models.ImageField(upload_to='evidences/', null=True)
    Working_Hour = models.PositiveIntegerField(null=True)
    Pay = models.PositiveIntegerField(null=True)
    Date = models.DateField(null=True, blank=True, help_text='Please enter in the format mm/dd/yyyy')

    def get_absolute_url(self):
        """Returns the url to access a particular author instance."""
        return reverse('noti_detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model Object."""
        return str(self.id)





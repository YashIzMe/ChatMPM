from django.db import models
from django.contrib.auth.models import Group

from accounts.models import Account

# Create your models here.
class ChatGroup(Group):
    """ extend Group model to add extra info"""
    users = models.ManyToManyField(Account)
    description = models.TextField(blank=True, help_text="description of the group")
    mute_notifications = models.BooleanField(default=False, help_text="disable notification if true")
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('chat:room', args=[str(self.id)])
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import GroupAdmin as GroupAdminDefault

from .forms import GroupAdminForm
from .models import ChatGroup

# Unregister the original Group admin.
admin.site.unregister(Group)

# Register your models here.
class ChatGroupAdmin(admin.ModelAdmin):
    form = GroupAdminForm
    """ enable Chart Group admin """
    list_display = ('id', 'name', 'description', 'mute_notifications', 'date_created', 'date_modified')
    list_filter = ('id', 'name', 'description', 'mute_notifications', 'date_created', 'date_modified')
    list_display_links = ('name',)

    def save_model(self, request, obj, form, change):
        super(ChatGroupAdmin, self).save_model(request, obj, form, change)
        if 'users' in form.cleaned_data:
            form.instance.user_set.set(form.cleaned_data['users'])

admin.site.register(ChatGroup, ChatGroupAdmin)
from django import VERSION, forms
from django.contrib.admin.widgets import FilteredSelectMultiple
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

from .models import ChatGroup
from accounts.models import Account

User = get_user_model()

class GroupAdminForm(forms.ModelForm):
    users = forms.ModelMultipleChoiceField(
        queryset=User.objects.all(), 
        required=False,
        widget=FilteredSelectMultiple(
            verbose_name=_('Users'),
            is_stacked=False
        )
    )

    class Meta:
        model = ChatGroup
        fields = ('name','users')

    def __init__(self, *args, **kwargs):
        super(GroupAdminForm, self).__init__(*args, **kwargs)

        if self.instance and self.instance.pk:
            self.fields['users'].initial = self.instance.users.all()
    
    def clean_name(self):
        name = self.cleaned_data['name']
        try:
            chatgroup = ChatGroup.objects.exclude(pk=self.instance.pk).get(name=name)
        except ChatGroup.DoesNotExist:
            return name
        raise forms.ValidationError('Group Name "%s" is already in use.' %name)

    def clean_users(self):
        users = self.cleaned_data['users']
        return users    
from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from . models import ChatGroup
from accounts.models import Account
from .forms import GroupAdminForm
from .admin import ChatGroupAdmin

# Create your views here.
def get_members():
    """ function to get all participants that belong the specific group """
    
    temp_participants = []
    for participants in Account.objects.values_list('username', flat=True):
        temp_participants.append(participants)
    return temp_participants


def group(request):
    
    if request.POST:
        g = ChatGroup()
        form = GroupAdminForm(request.POST, instance=g)
        print(form.errors)
        if form.is_valid():
            new_group = form.save()
            if 'users' in form.cleaned_data:
                form.instance.user_set.set(form.cleaned_data['users'])

            return HttpResponseRedirect('')

    else:
        form = GroupAdminForm()

    print("The form isn't valid")
    return render(request, "chat/group.html", {"form" : form, "members" : get_members()})



def get_participants(group_id=None, group_obj=None, user=None):
    """ function to get all participants that belong the specific group """
    
    if group_id:
        chatgroup = ChatGroup.objects.get(id=id)
    else:
        chatgroup = group_obj

    temp_participants = []
    for participants in chatgroup.user_set.values_list('username', flat=True):
        if participants != user:
            temp_participants.append(participants.title())
    temp_participants.append('You')
    return ', '.join(temp_participants)


@login_required
def room(request, group_id):
    if request.user.groups.filter(id=group_id).exists():
        chatgroup = ChatGroup.objects.get(id=group_id)
        #TODO: make sure user assigned to existing group
        assigned_groups = list(request.user.groups.values_list('id', flat=True))
        groups_participated = ChatGroup.objects.filter(id__in=assigned_groups)
        return render(request, 'chat/room.html', {
            'chatgroup': chatgroup,
            'participants': get_participants(group_obj=chatgroup, user=request.user.username),
            'groups_participated': groups_participated
        })
    else:
        return HttpResponse("chat:unauthorized")

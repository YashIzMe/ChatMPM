from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from accounts.models import Account

# Create your views here.
def index(request):
    return render(request, 'chat/index.html')


@login_required
def room(request,user_id):
    if request.user:
        chatgroup = Account.objects.get(id=user_id)
        return render(request, 'chat/room.html', {
            'chatgroup': chatgroup,
            'groups_participated': list(Account.objects.exclude(username = request.user.username)),
        })
    else:
        return HttpResponse("chat:unauthorized")
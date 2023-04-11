from django.shortcuts import render 
# from django.contrib.auth.decorators import login_required 
from django.contrib.sessions.models import Session
from django.contrib.auth.models import User
from django.utils import timezone


# Create your views here.
# @login_required
def accountview(request): 
    return render(request,'booklist.html',{}) 

# @login_required
def contentview (request):
    return render (request,'contents.html',{}) 

def active_users(request):
    active_sessions = Session.objects.filter(expire_date__gte=timezone.now())
    user_ids = []
    for session in active_sessions:
        data = session.get_decoded()
        user_id = data.get('_auth_user_id', None)
        if user_id:
            user_ids.append(user_id)
    active_users = User.objects.filter(id__in=user_ids)
    usernames = [user.username for user in active_users]
    return render(request, 'activeusers.html', {'usernames': usernames})








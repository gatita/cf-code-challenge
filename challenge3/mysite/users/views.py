from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse

from users.models import User

def user_list(request):
    users = User.objects.all()
    return render(request, 'users/user_list.html', {'users': users})

from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.forms import ModelForm
from django.core.urlresolvers import reverse

from users.models import User

class AddUser(ModelForm):
    class Meta:
        model = User

def user_list(request):
    users = User.objects.all()
    return render(request, 'users/user_list.html', {'users': users})

def create(request):
    form = AddUser(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect(reverse('users:user_list'))
    return render(request, 'users/create.html', {'form': form})


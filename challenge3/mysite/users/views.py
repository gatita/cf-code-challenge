from django.shortcuts import render, get_object_or_404, redirect
from django.forms import ModelForm
from django.core.urlresolvers import reverse

from users.models import User

class UserForm(ModelForm):
    class Meta:
        model = User

def user_list(request):
    users = User.objects.all()
    return render(request, 'users/user_list.html', {'users': users})

def create(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect(reverse('users:user_list'))
    return render(request, 'users/create.html', {'form': form})

def edit(request, user_id):
    p = get_object_or_404(User, pk=user_id)
    form = UserForm(request.POST or None, instance=p)
    if form.is_valid():
        form.save()
        return redirect(reverse('users:user_list'))
    return render(request, 'users/edit.html', {'form': form})

def delete(request, user_id):
    p = get_object_or_404(User, pk=user_id)
    p.delete()
    return redirect(reverse('users:user_list'))





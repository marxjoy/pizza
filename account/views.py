from django.shortcuts import render
from .forms import UserRegistrationForm, UserEditForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def register(request):
    """
    Register new User view
    """
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            messages.success(request, 'New user created')
            return render(request,
                         'register/register_done.html',
                        {'new_user': new_user})
        else:
            messages.error(request, 'New user cannot be created')
    else:
        user_form = UserRegistrationForm()
    return render(request,
                 'register/register.html',
                 {'user_form': user_form})

@login_required
def edit(request):
    """
    Edit User view
    """
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user,
                                data=request.POST)
        if user_form.is_valid():
            user_form.save()
            messages.success(request, 'Data changed success')
        else:
            messages.error(request, 'Profile edit error')
            
    else:
        user_form = UserEditForm(instance=request.user)
        
    return render(request,
                 'profile/edit.html',
                 {'user_form': user_form,
                 })
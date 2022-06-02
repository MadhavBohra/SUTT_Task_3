from django.shortcuts import render, redirect

# we import user creation form so we don't have to make it from scratch
# this is classes that gets converted into html
#from django.contrib.auth.forms import UserCreationForm

# To display a flash message we inport this :
from django.contrib import messages

from .forms import UserRegisterForm



# Create your views here.


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('doubt-page-home')

        else:
            return render(request,'users_app/register.html',{'form': form})
    else:
        # we need to create a form, so that user can input the data
        form = UserRegisterForm()
        return render(request,'users_app/register.html',{'form': form})



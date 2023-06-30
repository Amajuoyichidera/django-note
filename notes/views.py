from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'notes/index.html')

def register(request):
    form=UserCreationForm()

    if request.method =='POST':
        form=UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request,f'Account created for {username}')
            return redirect('notes:login')
    context={
        'form':form,
    }
    return render(request, 'notes/register.html', context)


def settings(request):
    return render(request, 'notes/settings.html')

def loggedout(request):
    return render(request, 'notes/loggedout.html')

def update(request):
    return render(request, 'notes/update.html')

def home_page(request):
    return render(request, 'notes/home.html')
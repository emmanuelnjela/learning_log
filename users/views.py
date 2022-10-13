from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def register(request):
    """register new user"""
    if request.method != 'POST':
        """Display black registration form"""
        form = UserCreationForm()
    else:
        """Data submitted; process user data"""
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            # login new user in, then redirect to home page
            login(request, new_user)
            return redirect('learning_logs:index')

    # display black or invalid form
    context = {'form': form}
    return render(request, 'registration/register.html', context)

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

# Create your views here.
def register(request):
    # If the request is POST the form will be passed in
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        # If the form is valid the user will receive a prompt and be redirected to the homepage
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"{username}, your account has been created!")
            return redirect('storyteller-homepage')
        # If the form is NOT valid a registration form will be returned
    else:
        form = UserCreationForm()
    return render(request, 'users/registration.html', {'form': form})

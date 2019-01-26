from django.shortcuts import render, redirect
from .forms import SignupModelForm
from home.models import MyUser
from django.contrib import messages

# Create your views here.


def get_signup(request):
    form = SignupModelForm(request.POST or request.FILES or None)
    if form .is_valid():
        instance = form.save(commit=False)
        # Signup fields
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        phone_number = request.POST.get('phone_number')
        gender = request.POST.get('gender')
        password = request.POST.get('password')
        user = MyUser(
            first_name=first_name,
            last_name=last_name,
            username=username,
            phone_number=phone_number,
            gender=gender,
            password=password
        )

        user.set_password(password)
        user.save()
        messages.add_message(request, messages.SUCCESS, 'Registration successfully complete')
        return redirect('login')
    return render(request, 'signup.html', {"form": form})

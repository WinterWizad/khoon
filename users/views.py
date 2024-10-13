from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from django.http import HttpResponse
from django.contrib import messages

from newapp.global_vars import donor_processor
from .forms import DonerForm
from .models import Doners

# Create your views here.
def register_view(request):
    if request.method =="POST":
        form=UserCreationForm(request.POST)
        if form.is_valid():
            login(request,form.save())  #This registers and logins the user 
            return redirect("newapp:home")
    else:
        form=UserCreationForm()
    return render(request,"register.html",{"form":form})


def login_view(request):
    if request.method =="POST":
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request,form.get_user())
            if "next" in request.POST:
                return redirect(request.POST.get("next")) 
            # These two lines of code sees which page user was trying to go when our system asked him to login and send him directly there rather than default
            else:
                return redirect("newapp:posts")
    else:
        form=AuthenticationForm()
    return render(request,"login.html",{"form":form})

def logout_view(request):
    if request.method=="POST":
        logout(request)
        return redirect("newapp:home")


@login_required(login_url="/users/login/")
def donor_register(request):
     # Use the donor processor to get the donor data
    donor_data = donor_processor(request)  # This returns a dictionary
    donor = donor_data.get('donor')  # Get the donor queryset

    # Check if the donor queryset exists
    if donor and donor.exists():
        messages.info(request, "You are already a Donor! Thank you")
        return redirect("newapp:home")
    
    if request.method=="POST":
        form=DonerForm(request.POST,request.FILES)
        if form.is_valid():
            newdonor=form.save(commit=False)
            newdonor.username=request.user
            form.save()
            return redirect("newapp:home")
    else:
        form=DonerForm()
        
    return render(request,"donor.html",{"form":form})

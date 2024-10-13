from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import EmergenciesForm
from .models import Emergencies
from django.contrib.auth.decorators import login_required

from users.models import Doners
# Create your views here.


completed=0
def counting():
    required=Emergencies.objects.all().count()
    total=completed+required
    return {
        'total':total,
        'required_donors': required,
        'completed':completed
    }

donor=None
def index(request):   
    if (request.method=="POST"):
        print("YO") 
        address=request.POST.get('address')
        if address:
            donors = Doners.objects.filter(address=address)  # Make sure you have the address field set up correctly
        else:
            donors=Doners.objects.all()
        # Store the donors in the session if you need to access them later
        request.session['req_address'] = list(donors.values_list('id', flat=True))
        return redirect('newapp:donor_list')
    else:
        donor=Doners.objects.filter(username__username=request.user.username)
        counters=counting()
        print("hi")
        return render(request,'index.html',{"donor":donor,"counters":counters })  

def donor_list(request):
    # Get donor IDs from the session
    print("here is donor list")
    address = request.session.get('req_address', [])
    donors = Doners.objects.filter(id__in=address)  # Retrieve donors by their IDs
    return render(request, 'donor_list.html', {"donors": donors})

def emergency(request):
     applications=Emergencies.objects.all()   
     data={
        "applications": applications,
        "user":request.user,
        "donor":donor
     }    
     required=len(data)
     return render(request,'emergency.html',data)

@login_required(login_url="/users/login/")
def submission(request):     
     if(request.method == "POST"):
        form=EmergenciesForm(request.POST, request.FILES)
        if form.is_valid():
           newpost=form.save(commit=False)
           newpost.author=request.user
           form.save()
           return redirect('newapp:posts')  
     else:
         form=EmergenciesForm()   
     return render(request,'submission.html',{"form":form})


def dlt_std(request,id):
    global completed
    try:
        patient=Emergencies.objects.get(id=id)
        patient.delete()
        completed += 1
        return redirect('newapp:posts')
    except:
        return HttpResponse("NO Page")    

def post_page(request,slug):
    post=Emergencies.objects.get(slug=slug)
    return render(request, 'post.html',{'post':post})

from .models import Person,  Referral
from django.shortcuts import redirect, render
from .forms import PersonForm,  ReferralForm, AddReferralForm
from django.contrib.auth.decorators import login_required

from nz_health import forms

# Create your views here.
# Home to render general info

def home (request):
    return render(request, "nz_health/home.html");



#Person
@login_required(login_url='/login')
def person (request):
    person = Person.objects.all()
    return render(request, "nz_health/person.html", {"person":person});
@login_required
def person_details (request, id):   
    person_details = Person.objects.get(pk = id)
    referral_form = ReferralForm()
    return render(request, "nz_health/person_details.html", 
        {
            "person_details":person_details,
            "referral_form":referral_form,
        });
# POST and GET request
# Create new person or get the list of person
@login_required(login_url='/login')
def person_form (request, id=0):
    #POST request
    if request.method == 'POST':
        #Create new Person
        if id == 0:
            person_form = PersonForm(request.POST)
        #Update/Edit Person
        else:
            person = Person.objects.get(pk=id)
            person_form = PersonForm(request.POST, instance=person)
        if person_form.is_valid():
            person_form.save()
        return redirect('/person')
    #GET request       
    else:
        if id == 0:
            person_form = PersonForm()
        #GET a Person
        else:
            person = Person.objects.get(pk=id)
            person_form = PersonForm(instance=person)
    return render(request, 'nz_health/person_form.html',{'person_form': person_form})

@login_required(login_url='/login')
def person_delete (request, id):
    person = Person.objects.get(pk=id)
    person.delete()
    return redirect('/person')

#Referrals

@login_required(login_url='/login')
def referrals (request):
    referrals = Referral.objects.all()
    return render(request, "nz_health/referrals.html", {"referrals":referrals});


# def referral_form (request):
   # return render(request, "nz_health_app/referral_form.html");

@login_required(login_url='/login')
def referral_form (request, id=0):
    if request.method == 'POST':
        if id == 0:
            referral_form = AddReferralForm(request.POST)
        else:
            referrals = Referral.objects.get(pk=id)
            referral_form = AddReferralForm(request.POST, instance=referrals)
        if referral_form.is_valid():
            referral_form.save()
        return redirect('/referrals')       
    else:
        if id == 0:
            referral_form = AddReferralForm()
        else:
            referrals = Referral.objects.get(pk=id)
            referral_form = AddReferralForm(instance=referrals)
    return render(request, 'nz_health/referral_form.html',{'referral_form': referral_form})


@login_required(login_url='/login')
def referral_delete (request, id):
    referral_delete = Referral.objects.get(id=id)
    if request.method == "POST":
        referral_delete.delete()
        return redirect('/referrals')
    return render(request, "nz_health/referral_delete.html", {"referral_delete":referral_delete});

@login_required(login_url='/login')
def referral_details (request, id):   
    referral_details = Referral.objects.filter(pk=id)
    return render(request, "nz_health/referral_details.html", {"referral_details":referral_details});

@login_required(login_url='/login')
def add_referral (request, person_id):
    # Create ModelForm using the data in the request.POST
    form = ReferralForm(request.POST)
    #validate the form
    if form.is_valid():
        new_referral = form.save(commit=False)
        new_referral.person_id = person_id
        new_referral.save()
    return redirect('person_details', id=person_id)
    
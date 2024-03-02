from django.shortcuts import render, redirect
from .models import  Baby, Allergy, Vaccine_Month, Vaccine,User, Vaccined_Baby
from .forms import Add_Baby_Form, Log_In_Form, Sign_In_Form
from datetime import date
from django.db.models import Sum
from django.urls import reverse


def log_in(request):
    log_in_form_sent = request.POST.get('log_in_form')
    if log_in_form_sent:
        form = Log_In_Form(request.POST)
        if form.is_valid():
            tmp = form.save(commit=False) 
            user_exists = User.objects.filter(pseudo=tmp.pseudo)
            if user_exists:
                if tmp.mot_passe == user_exists.mot_passe:
                    return redirect(reverse("bienvenu", args=[user_exists.id]))
    else:
        form = Log_In_Form()
        return render(request,'login.html',{"form":form})
    message = "error"
    return render(request,'login.html',{"message":message})

def signin(request):
    sign_in_form_sent = request.POST.get('sign_in_form')
    if sign_in_form_sent:
        form = Sign_In_Form(request.POST)
        tmp = form.save(commit=False) 
        exists = User.objects.filter(pseudo=tmp.pseudo).first()
        if exists == None:
            if form.is_valid():
                user = form.save()
                return redirect(reverse("bienvenu", args=[user.id]))
    else:
        form = Sign_In_Form()
        return render(request,'signin.html',{"form":form})
    message = "error"
    return render(request,'signin.html',{"message":message})

def bienvenu(request, pk):
    user = User.objects.get(id=pk)
    list_enfants = Baby.objects.filter(associated_user=user)
    return render(request,'bienvenu.html',{"list_enfants":list_enfants})

def add_baby_general(request, pk):
    if request.method == 'POST':
        form = Add_Baby_Form(request.POST)
        if form.is_valid():
            tmp = form.save()
            return redirect(reverse("remplir_vacsination", args=[pk, tmp.id]))
    else:
        form = Add_Baby_Form()
        allergies = Allergy.objects.all()
    return render(request, "add_baby.html", {"form": form, "allergies": allergies})

def remplir_vacsination(request, pk1, pk2):
    vaccines = Vaccine.objects.all()
    return render(request,'remplir_vacsination.html',{"vaccines":vaccines, "pk2":pk2})

def calendrier(request, pk1, pk2):
    none_vaccined_Months = []
    vaccined_Months = []
    months = Vaccine_Month.objects.all()
    for vm in months:
        b = 0
        Vaccine_for_vm = Vaccine.objects.filter(month=vm)
        for v in Vaccine_for_vm:
            # idk if this would work alone without specifying the parent
            exist = Vaccined_Baby.objects.filter(associated_baby_vb=pk2, vaccine_vb=v)
            if exist == None:
                none_vaccined_Months.append(vm)
                b = 1
        if b == 0:
            vaccined_Months.append(vm)
    return render(request, "calendrier.html", {"none_vaccined_Months": none_vaccined_Months, "vaccined_Months": vaccined_Months})
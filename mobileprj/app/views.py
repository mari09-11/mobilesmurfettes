from django.shortcuts import render, redirect
from .models import  Baby, Allergy, Vaccine_Month, Vaccine,User, Vaccined_Baby
from .forms import Add_Baby_Form, Log_In_Form, Sign_In_Form
# from datetime import date
from django.urls import reverse


def log_in(request):
    if request.method == "POST":
        form = Log_In_Form(request.POST)
        if form.is_valid():
            tmp = form.save(commit=False) 
            user_exists = User.objects.filter(pseudo=tmp.pseudo).first()
            if user_exists:
                if tmp.mot_passe == user_exists.mot_passe:
                    return redirect("/bienvenu/{}/".format(user_exists.id))
                else:
                    form = Log_In_Form()
                    message = "wrong pass word"
                    return render(request,'login.html',{"message":message, "form":form})
    else:
        form = Log_In_Form()
        return render(request,'login.html',{"form":form})
    form = Log_In_Form()
    message = "this account doesnt exist"
    return render(request,'login.html',{"message":message, "form":form})

def sign_in(request):
    if request.method == "POST":
        form = Sign_In_Form(request.POST)
        tmp = form.save(commit=False) 
        exists = User.objects.filter(pseudo=tmp.pseudo).first()
        if exists == None:
            if form.is_valid():
                tmp.save()
                return redirect("/bienvenu/{}/".format(tmp.id))
            else:
                message = "fill all the input areas"
                form = Sign_In_Form()
                return render(request,'signin.html',{"message":message, "form":form})
        else:
            form = Sign_In_Form()
            message = "that user name is already taken"
            return render(request,'signin.html',{"message":message, "form":form})
    else:
        form = Sign_In_Form()
        return render(request,'signin.html',{"form":form})

def bienvenu(request, user_id):
    user = User.objects.get(id=user_id)
    list_enfants = Baby.objects.filter(associated_user=user)
    return render(request,'bienvenu.html',{"list_enfants":list_enfants})

def add_baby_general(request, user_id):
    if request.method == 'POST':
        form = Add_Baby_Form(request.POST)
        if form.is_valid():
            tmp = form.save()
            return redirect(reverse("remplir_vacsination", args=[user_id, tmp.id]))
    else:
        form = Add_Baby_Form()
        allergies = Allergy.objects.all()
    return render(request, "add_baby.html", {"form": form, "allergies": allergies})

def remplir_vacsination(request, user_id, baby_id):
    vaccines = Vaccine.objects.all()
    return render(request,'remplir_vacsination.html',{"vaccines":vaccines, "baby_id":baby_id})

def calendrier(request, user_id, baby_id):
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

def vaccine_month(request, user_id, baby_id, month_id):
    vaccined_vaccines = []
    none_vaccined_vaccines = []
    month = Vaccine_Month.objects.get(id=month_id)
    Vaccine_for_vm = Vaccine.objects.filter(month=month)
    for v in Vaccine_for_vm:
        # idk if this would work alone without specifying the parent
        exist = Vaccined_Baby.objects.filter(associated_baby_vb=baby_id, vaccine_vb=v)
        if exist == None:
            none_vaccined_vaccines.append(month)
        else:
            vaccined_vaccines.append(month)
    return render(request, "calendrier.html", {"none_vaccined_vaccines": none_vaccined_vaccines, "vaccined_vaccines": vaccined_vaccines})


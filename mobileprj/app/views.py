from django.shortcuts import render, redirect
from .models import  Baby, Allergy, Vaccine_Month, Vaccine,User
from .forms import Add_Baby_Form, Check_Vaccine_beginning_Form, Check_Vaccine_Form, Log_In_Form, Sign_In_Form
from datetime import date
from django.db.models import Sum
from django.urls import reverse

    # path("sautentifier/login/", views.log_in),
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

    # path("sautentifier/signin/", views.signin),
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

    # path("bienvenu/", views.bienvenu),
    # path("add_baby/general/", views.add_baby_general),
    # path("add_baby/remplir_vacsination/", views.add_baby_remplir_vacsination),
    # path("calendrier/", views.calendrier),
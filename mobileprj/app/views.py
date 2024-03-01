from django.shortcuts import render
from .models import  Baby, Allergy, Vaccine_Month, Vaccine
from .forms import Add_Baby, Check_Vaccine_beginning, Check_Vaccine
from datetime import date
from django.db.models import Sum

    # path("sautentifier/login/", views.log_in),
def log_in(request, pk):
    stock=User.objects.get(id=pk)
    if request.method=='POST':
        form =StockForm(request.POST, instance=stock)
        if form.is_valid():
            form.save()
            return redirect("stock")
    else:
        form=StockForm(instance=stock)
        return render(request,'editStock.html',{"form":form})

    # path("sautentifier/signin/", views.signin),
    # path("bienvenu/", views.bienvenu),
    # path("add_baby/general/", views.add_baby_general),
    # path("add_baby/remplir_vacsination/", views.add_baby_remplir_vacsination),
    # path("calendrier/", views.calendrier),
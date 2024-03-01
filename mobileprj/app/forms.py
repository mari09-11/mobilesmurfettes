from django import forms
from .models import Baby, Allergy, Vaccine_Month, Vaccine, User

class Log_In_Form(forms.ModelForm):
    class Meta:
        model = User
        fields = ['pseudo', 'mot_passe']

class Sign_In_Form(forms.ModelForm):
    class Meta:
        model = User
        fields = "__all__"

class Add_Baby_Form(forms.ModelForm):
    class Meta:
        model = Baby
        fields = "__all__"

class Check_Vaccine_beginning_Form(forms.ModelForm):
    class Meta:
        model = Vaccine
        fields = ['nom_v', 'date']

class Check_Vaccine_Form(forms.ModelForm):
    class Meta:
        model = Vaccine
        fields = ['est_fait']
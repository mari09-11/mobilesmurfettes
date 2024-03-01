from django import forms
from .models import Baby, Allergy, Vaccine_Month, Vaccine, User

class Log_In(forms.ModelForm):
    class Meta:
        model = User
        fields = ['pseudo', 'mot_passe']

class Sign_in(forms.ModelForm):
    class Meta:
        model = User
        fields = "__all__"

class Add_Baby(forms.ModelForm):
    class Meta:
        model = Baby
        fields = "__all__"

class Check_Vaccine_beginning(forms.ModelForm):
    class Meta:
        model = Vaccine
        fields = ['nom_v', 'date']

class Check_Vaccine(forms.ModelForm):
    class Meta:
        model = Vaccine
        fields = ['est_fait']
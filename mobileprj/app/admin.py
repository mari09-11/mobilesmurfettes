from django.contrib import admin
from .models import Baby, Allergy, Vaccine_Month, Vaccine, Sexe, Groupe_Sanguin, User

admin.site.register(Baby)
admin.site.register(Allergy)
admin.site.register(Vaccine_Month)
admin.site.register(Vaccine)
admin.site.register(Sexe)
admin.site.register(Groupe_Sanguin)
admin.site.register(User)

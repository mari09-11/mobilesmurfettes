from django.db import models

class Baby(models.Model):
    nom_b = models.CharField(max_length= 50),
    date_naissance = models.DateTimeField(auto_now=True),
    sexe = models.CharField(max_length= 50),
    groupe_sanguin = models.CharField(max_length= 50),
    def __str__(self):
        return str(self.nom_b)

class Allergy(models.Model):
    nom_a = models.CharField(max_length= 50),
    associated_baby_a = models.ForeignKey(Baby, on_delete=models.CASCADE),
    def __str__(self):
        return str(self.nom_a)

class Vaccine_Month(models.Model):
    nom_vm = models.IntegerField(),
    def __str__(self):
        return str(self.nom_vm)

class Vaccine(models.Model):
    nom_v = models.CharField(max_length= 50),
    month = models.ForeignKey(Vaccine_Month, on_delete=models.CASCADE),
    est_fait = models.BooleanField(),
    associated_baby_v = models.ForeignKey(Baby, on_delete=models.CASCADE),
    def __str__(self):
        return str(self.nom_v)
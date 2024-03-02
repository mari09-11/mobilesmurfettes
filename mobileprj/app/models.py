from django.db import models

class Sexe(models.Model):
    nom_s = models.CharField(max_length = 10),
    def __str__(self):
        return str(self.nom_s)

class Groupe_Sanguin(models.Model):
    nom_gs = models.CharField(max_length = 2),
    def __str__(self):
        return str(self.nom_gs)

class User(models.Model):
    pseudo = models.CharField(max_length = 20)
    mot_passe = models.CharField(max_length = 50)
    Email = models.CharField(max_length = 100)
    def __str__(self):
        return str(self.pseudo)

class Baby(models.Model):
    nom_b = models.CharField(max_length = 20),
    date_naissance = models.DateTimeField(),
    sexe = models.ForeignKey(Sexe, on_delete = models.CASCADE),
    groupe_sanguin = models.ForeignKey(Groupe_Sanguin, on_delete = models.CASCADE),
    associated_user = models.ForeignKey(User, on_delete = models.CASCADE),
    def __str__(self):
        return str(self.nom_b)

class Allergy(models.Model):
    nom_a = models.CharField(max_length = 50),
    def __str__(self):
        return str(self.nom_a)

class Allergic_Baby(models.Model):
    allergy_ab = models.ForeignKey(Allergy, on_delete = models.CASCADE),
    associated_baby_ab = models.ForeignKey(Baby, on_delete = models.CASCADE),

class Vaccine_Month(models.Model):
    nom_vm = models.IntegerField(),
    def __str__(self):
        return str(self.nom_vm)

class Vaccine(models.Model):
    nom_v = models.CharField(max_length = 50),
    date = models.DateTimeField(default=None),
    month = models.ForeignKey(Vaccine_Month, on_delete = models.CASCADE),
    def __str__(self):
        return str(self.nom_v)

class Vaccined_Baby(models.Model):
    vaccine_vb = models.ForeignKey(Vaccine_Month, on_delete = models.CASCADE),
    associated_baby_vb = models.ForeignKey(Baby, on_delete = models.CASCADE),
    date = models.DateTimeField(),
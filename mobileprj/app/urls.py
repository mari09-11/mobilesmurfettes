from django.urls import path
from . import views

urlpatterns = [
    # welcome would be only with react native
    path("sautentifier/login/", views.log_in),
    path("sautentifier/signin/", views.signin),
    path("bienvenu/", views.bienvenu),
    path("add_baby/general/", views.add_baby_general),
    path("add_baby/remplir_vacsination/", views.add_baby_remplir_vacsination),
    # home would be only with react native
    path("calendrier/", views.calendrier),
]

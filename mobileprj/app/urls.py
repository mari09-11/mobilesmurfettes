from django.urls import path
from . import views

urlpatterns = [
    # welcome would be only with react native
    path("sautentifier/login/", views.log_in, name='login'),
    path("sautentifier/signin/", views.sign_in, name='signin'),
    path("bienvenu/<int:user_id>/", views.bienvenu, name='bienvenu'),
    path("add_baby/general/<int:user_id>/", views.add_baby_general),
    path("add_baby/remplir_vacsination/<int:user_id>/<int:baby_id>/", views.remplir_vacsination),
    # home would be only with react native
    path("calendrier/<int:user_id>/<int:baby_id>/", views.calendrier),
    path("calendrier/<int:user_id>/<int:baby_id>/<int:month_id>/", views.vaccine_month),
]

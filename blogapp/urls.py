from django.urls import path
from blogapp import views

app_name='blogapp'

urlpatterns = [
   path('', views.acceuil_view, name='accueil'),
    path('inscription/',views.inscription_view,name='inscription'),
    path('connexion/',views.connexion_view,name='connexion'),
    path('deconnexion/',views.deconnexion_view,name='deconnexion')
    
]

from django.urls import path
from . import views


urlpatterns = [
    path('', views.homePage, name="home"),
    path('projectview/<str:pk>', views.projectview, name="projectview"),
    path('aboutMe/', views.aboutMe, name="aboutMe"),
    path('allprojects/', views.allprojects, name="allprojects"),
    path('gallery/', views.gallery, name="gallery"),
    path('contact/', views.contact, name="contact"),
   
]

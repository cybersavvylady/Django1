# This is the project urls file, must not have any reference to admin
#Each app needs to have a default path
from django.urls import path
from . import views

urlpatterns = [
    path("", views.Home)

]
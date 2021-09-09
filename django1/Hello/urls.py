from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("jacob/", views.jacob, name="jacob"),
    path("<str:name>/", views.greet, name="greet")
]
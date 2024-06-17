from django.urls import path
from .import views


urlpatterns = [
    path('getallcharacter/',views.getallcharacter.as_view()),
    path('createcharacter/',views.createcharacter.as_view())

]
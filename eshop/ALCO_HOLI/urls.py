from django.urls import path
from .import views


urlpatterns = [
    path('getallinstrument/',views.getallinstrument.as_view()),
    #path('getspecificinstrument/<instrument_name>',views.getspecificinstrument.as_views())
]
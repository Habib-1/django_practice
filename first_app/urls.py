from django.urls import path
from .import views
urlpatterns = [
    path('hired',views.hired),
    path('hire_teams',views.hire_team)
   
]
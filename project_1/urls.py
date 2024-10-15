from django.contrib import admin
from django.urls import path, include
from .import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/',views.about),
    path('contact', views.contact),
    path("",views.homepage),
    path('first_app/',include("first_app.urls"))
   
]

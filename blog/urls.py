from django.urls import path
from blog import views

app_name = "blog"

urlpatterns = [
    path("",views.Homeview,name="home"),
    path("brenda/",views.contacts,name="contact"),
    # path("salma/",views.AboutUs,name="location"),
]

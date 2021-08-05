from django.urls import path
from blog import views

app_name = "blog"

urlpatterns = [
    path("", views.HomeView, name='home'),
    path("about/", views.AboutUsView, name="about"),
    path("contact/", views.ContactUsView, name="contact"),
]

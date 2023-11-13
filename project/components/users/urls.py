from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path("submit_form", views.submit_form, name="submit_form"),
    path("submit_remove_user/<str:id>", views.submit_remove_user, name="submit_remove_user"),
    path("redirect/<str:id>", views.redirect_update_page, name="redirect_update_page"),
    path("redirect/submit_update_form/<str:id>", views.submit_update_form, name="submit_update_form")
]
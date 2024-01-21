from django.urls import path
from little_app import views

app_name = "lil"

urlpatterns = [
    path("other/", views.other, name="other"),
]

from django.urls import path, re_path
from .views import BookApiView

# app_name = AppName

urlpatterns = [
    path("", BookApiView.as_view(), name="")
]
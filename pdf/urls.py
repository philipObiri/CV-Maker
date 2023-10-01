from django.urls import path 
from . import views


urlpatterns = [
    path("", views.create_cv, name="create_cv"),
    path("resume/<int:id>", views.generated_cv_view, name="resume"),
    path("profiles/", views.list_of_profiles, name="profiles"),
]

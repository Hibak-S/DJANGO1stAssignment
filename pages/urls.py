from django.urls import path
from . import views  # Import views from the current app

# This is where you map URLs to your view functions
urlpatterns = [
    # Maps the root URL ('') to the index_view
    path("", views.index_view, name="index"),
    # Maps the 'education/' URL to the education_view
    path("education/", views.education_view, name="education"),
]

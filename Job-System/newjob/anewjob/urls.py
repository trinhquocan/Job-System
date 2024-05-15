from django.urls import path, re_path, include
from . import views

urlpatterns = [
    path('anewjob/', views.index, name="index"),
    path('anewjob/<int:job_id>', views.list, name="list"),
    path('category/', views.CategoryView.as_view())
]
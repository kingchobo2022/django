
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('<int:member_id>/', views.detail)
]

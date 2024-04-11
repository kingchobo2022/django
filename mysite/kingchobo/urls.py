
from django.urls import path

from . import views

app_name = 'kingchobo'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:member_id>/', views.detail, name='detail')
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.CommuneHistoryList.as_view(), name='commune-history-list'),
]
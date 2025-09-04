from django.urls import path
from . import views

urlpatterns = [
    path('communeHistory/', views.CommuneHistoryList.as_view(), name='commune-history-list'),
    path('', views.index, name='index'),
]
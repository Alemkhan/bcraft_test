from django.urls import path
from .views import (
    StatisticsCreateView,
    StatisticsListView,
    StatisticsResetView
)

urlpatterns = [
    path('', StatisticsListView.as_view(), name='statistics_list'),
    path('create', StatisticsCreateView.as_view(), name='statistics_create'),
    path('reset', StatisticsResetView.as_view(), name='statistics_reset')
]

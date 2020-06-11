from django.urls import path
from goozs.views import (
    GoozsCreateView,
    GoozsIndexView,
)

urlpatterns = [
    path('', GoozsIndexView.as_view(), name='index'),
    path('register/', GoozsCreateView.as_view(), name='register'),
]

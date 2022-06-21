from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("get_user_data/<str:wallet_address>",
         views.get_user_data, name="get_user_data"),
    path("get_buy_history/<str:wallet_address>",
         views.get_buy_history, name="get_buy_history"),
]

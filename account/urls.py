from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_account, name='register_account'),
    path('', views.get_accounts, name='get_accounts'),
    path('<int:pk>', views.get_account_by_pk, name='account_pk'),
    path('update/<int:pk>', views.update_account_by_pk, name='update_account'),
    path('<int:pk>', views.delete_account_by_pk, name='delete_account'),
]

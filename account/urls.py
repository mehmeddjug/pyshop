from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_account, name='register_account'),
    path('account/', views.get_accounts, name='get_accounts'),
    path('account/<int:pk>', views.get_account_by_pk, name='account_pk'),
    path('account/<int:pk>', views.update_account_by_pk, name='update_account'),
    path('account/<int:pk>', views.delete_account_by_pk, name='delete_account'),
]

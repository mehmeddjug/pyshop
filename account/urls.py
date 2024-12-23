from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_account, name='register_account'),
    path('', views.get_accounts, name='get_accounts'),
    path('<int:account_id>/', views.get_account_by_id, name='get_account_by_id'),
    path('update/<int:account_id>/', views.update_account_by_id, name='update_account'),
    path('delete/<int:account_id>/', views.delete_account_by_id, name='delete_account'),
    path('restore/<str:username>', views.restore_account, name='restore_account'),
]

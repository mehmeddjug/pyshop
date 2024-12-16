from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_account, name='register_account'),
    path('', views.get_accounts, name='get_accounts'),
    path('<int:id>/', views.get_account_by_id, name='get_account_by_id'),
    path('update/<int:id>/', views.update_account_by_id, name='update_account'),
    path('<int:id>/', views.delete_account_by_id, name='delete_account'),
    path('restore/<str:username>', views.restore_account, name='restore_account'),
]

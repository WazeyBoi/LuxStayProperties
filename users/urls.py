from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('tenant-management/', views.tenant_management, name='tenant_management'),
    path('tenant-landing/', views.tenant_landing_page, name='tenant_landing'),
    path('view-lease/<int:tenant_id>/', views.view_tenant_lease, name='view_tenant_lease'),
    path('edit-account/', views.edit_account, name='edit_account'),
]

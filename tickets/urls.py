from django.urls import path
from . import views

urlpatterns = [
    path('customer/', views.customer_dashboard, name='customer_dashboard'),
    path('customer/open/', views.open_ticket, name='open_ticket'),
    path('support/', views.support_dashboard, name='support_dashboard'),
    path('support/update/<int:ticket_id>/', views.update_ticket_status, name='update_ticket'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.customer_list, name='customer_list'),          
    path('<int:pk>/', views.customer_detail, name='customer_detail'),  # View details of a single product
    path('create/', views.customer_create, name='customer_create'),    # Create a new product
    path('<int:pk>/update/', views.customer_update, name='customer_update'),  # Update an existing product
]
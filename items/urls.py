from django.urls import path
from . import views

app_name = 'items'  # This is important for namespacing

urlpatterns = [
    path('', views.home, name='home'),  # Add this line for home page
    path('items/', views.item_list, name='item_list'), 
    path('items/new/', views.item_create, name='item_create'),
    path('items/<int:pk>/', views.item_detail, name='item_detail'),
    path('items/<int:pk>/edit/', views.item_update, name='item_update'),
    path('items/<int:pk>/delete/', views.item_delete, name='item_delete'),
]
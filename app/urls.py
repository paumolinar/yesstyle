from django.urls import path
from django.contrib.auth import views as auth_views 
from app import views

app_name = 'app'

urlpatterns = [
    path('', views.home, name='home'),
    path('product_detail/<int:product_id>', views.product_detail, name='product_detail'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('shopping_bag/', views.shopping_bag, name='shopping_bag'),
]

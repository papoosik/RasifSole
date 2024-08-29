
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index_view, name='index'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.signup_view, name='signup'),
    path('cart/', views.cart_view, name='cart_view'),
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('detail/<int:pk>/', views.detail_view, name='detail'),
    path('catalogue/<str:title_of_category>/', views.catalog_view, name='catalog'),
    path('create_shoes/', views.create_shoes, name='create_shoes'),
    path('update-shoes/<int:shoes_id>/', views.update_shoes, name='update_shoes'),
    path('delete-shoes/<int:shoes_pk>/', views.delete_shoes, name='delete_shoes')
]

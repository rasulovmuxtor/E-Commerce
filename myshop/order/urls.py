from django.urls import path
from . import views


urlpatterns = [
    path('', views.create_order, name='create_order'),
    path('admin/order/<int:order_id>/',views.admin_order_detail,name='admin_order_detail'),
    
]
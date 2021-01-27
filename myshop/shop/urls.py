from django.urls import path
from . import views

urlpatterns = [
    path('',views.dashboard,name='home'),
    path('<slug:slug>',views.category,name='category'),
    path('<slug:slug>/<slug:subslug>',views.subcategory,name='subcategory'),
    path('<slug:slug>/<slug:subslug>/<slug:item_slug>/',views.item_view,name='item_view'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('api/', views.ApiOverview),
    path('api/all/', views.get_all_item_data),
    path('api/create/', views.create_item, name='create'),
    path('api/delete/<int:id>/', views.delete_item),
    path('api/update/<int:id>/', views.update_item),
    path('api/detail/<int:id>/', views.get_item_data),
]
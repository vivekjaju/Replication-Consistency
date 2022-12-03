from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add, name='add'),
    path('add/addrecord/', views.addrecord, name='addrecord'),
    path('delete/<fname>/', views.delete, name='delete'),
    # path('delete2/<int:id>', views.delete, name='delete'),

    # path('add/order', views.index, name='index'),
    # path('buy/', views.index, name='buy'),
]
from django.urls import path
from .views import home, create, edit, update, delete

urlpatterns = [
    path('', home, name='home'),
    path('create', create, name='create'),
    path('edit/<int:id>/', edit, name='edit'),
    path('update/<int:id>/', update, name='update'),
    path('delete/<int:id>/', delete, name='delete'),
    
]
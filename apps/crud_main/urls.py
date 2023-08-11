from django.urls import path
from .views import list_todos, create_todos, delete_todos, update_todos

urlpatterns = [
    path('', list_todos),
    path('create/', create_todos),
    path('delete/<int:pk>/', delete_todos),
    path('update/<int:pk>/', update_todos),
]

from django.urls import path
from .views import hello_world, home, todoListCreate, todoList, todoCreate, todoUpdate,todoDelete


urlpatterns = [
    path('', home),
    path('hello/', hello_world),
    path('todoList/', todoList),
    path('todoCreate/', todoCreate),
    path('todoListCreate/', todoListCreate),
    path('todoUpdate/<int:pk>/', todoUpdate),
    path('todoDelete/<int:pk>/', todoDelete),
    
]

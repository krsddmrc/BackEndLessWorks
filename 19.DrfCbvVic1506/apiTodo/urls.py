from django.urls import path,include
from .views import ( 
    TodoMVS,
    home,
    #hello_world,
    #todoList,
    #todoCreate, 
    #todoListCreate, 
    #todoUpdate, 
    #todoDelete, 
    #TodoDetail,
    #TodoListCreate, 
    #TodoGetUpdateDelete
    )
from rest_framework import routers

router=routers.DefaultRouter() #! =routers.SimpleRouter() şeklide olur
router.register('todos',TodoMVS)  #! iki paremetre 1. prefix, 2. viewset

urlpatterns = [
    path('', home),
    #! function-based views
    #path('hello/', hello_world),
    #path('todoList/', todoList),
    #path('todoCreate/', todoCreate),
    #path('todoListCreate/', todoListCreate),
    #path('todoUpdate/<int:pk>/', todoUpdate),
    #path('todoDelete/<int:pk>/', todoDelete),

    #! class-based views
    #path('list/', TodoListCreate.as_view()), #!class-based olunca as_view() diyorduk
    #path('detail/<int:id>', TodoGetUpdateDelete.as_view()), 
    #path('detail/<int:id>', TodoDetail.as_view()),

    #! viewset path
    #path('todo',  TodoMVS )
   
    #path('', include(router.urls)) #! böyle olabilir

]
urlpatterns+=router.urls   #! yada böyle de eklenebilir.

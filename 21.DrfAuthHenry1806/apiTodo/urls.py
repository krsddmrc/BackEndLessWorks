from django.urls import path, include
from .views import home, TodoMVS
from rest_framework import routers

router = routers.DefaultRouter()
router.register('todos', TodoMVS )


urlpatterns = [
  
    #* Class Based Views
     path('', include(router.urls))
]



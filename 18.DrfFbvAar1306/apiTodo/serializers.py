from rest_framework import serializers    
from .models import Todo

class TodoSerializer(serializers.ModelSerializer): #! Todo modelden seralizers ürettim.
    class Meta:
        model=Todo
        fields= "__all__"

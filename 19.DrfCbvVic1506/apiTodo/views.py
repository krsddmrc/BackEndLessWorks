from django.http.response import HttpResponse
from django.shortcuts import render, get_object_or_404
import rest_framework
from rest_framework import serializers


from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Todo
from .serializers import TodoSerializer

from rest_framework import status
from rest_framework.views import APIView  #! class_based views için almıştım
from rest_framework import mixins       #! CBV mixins için almıştım
from rest_framework.generics import GenericAPIView #! CBV genericAPIview  için almıştım
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView #! CBV concrete views  için almıştım
from rest_framework import viewsets
from rest_framework.decorators import action

# Create your views here.
def home(request):
    return HttpResponse(
        '<center><h1 style="background-color:powderblue;">Welcome to ApiTodo</h1></center>'
    )

#! Function_based views are  under comments from 20 to 93
'''@api_view()
def hello_world(request):
    return Response({"message": "Hello, world!"})

@api_view(['GET'])
def todoList(request):
    querset =  Todo.objects.all()    
    serializer = TodoSerializer(querset, many=True)
   
    return Response(serializer.data)


@api_view(['POST'])
def todoCreate(request):

    serializer = TodoSerializer(data = request.data)
    
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['GET', 'POST'])
def todoListCreate(request):
    if request.method == "GET":
        querset =  Todo.objects.all()    
        serializer = TodoSerializer(querset, many=True)
    
        return Response(serializer.data)
    
    elif request.method == "POST":
        serializer = TodoSerializer(data = request.data)
    
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

@api_view(['GET','PUT', 'DELETE'])
def todoUpdate(request, pk):
    
    querset =  Todo.objects.get(id = pk)
    
    if request.method == "GET":
        serializer = TodoSerializer(querset)
    
        return Response(serializer.data)
        
    elif request.method == "PUT":
        
        serializer = TodoSerializer(instance=querset,  data = request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
            
        return Response(serializer.errors, status=status.HTTP_204_NO_CONTENT)
    
    elif request.method == "DELETE":
      
        querset.delete()
        return Response("Item Deleted")
        
    

@api_view(['DELETE'])
def todoDelete(request, pk):
    
    querset =  Todo.objects.get(id = pk)
    querset.delete()
    return Response("Item Deleted")'''
    
#! class-based  views begin here    
'''class TodoList(APIView): #! ctrl+ soltık ile inherit ettiği classlr görülebilir.
    def get(self, request):
        todos = Todo.objects.all()
        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)    #! url bağladıktan sonra get post yaptım çalıtı

class TodoDetail(APIView):
    # get_object_or_404 : Calls get() on a given model manager, but it raises Http404 instead of the model’s DoesNotExist exception.
    def get(self, id):
        todo = get_object_or_404(id=id)  #!birinci parametre hangi modelden , ikinci parametre neye göre alınacağı

    def get(self, request, id):
        todo = Todo.objects.get(id=id)
        serializer = TodoSerializer(todo)
        return Response(serializer.data)

    def put(self, request, id):
        todo = self.get_obj(id) #! burada kullandım, id ile get yapacak yoksa hata verecek.
        serializer = TodoSerializer(instance=todo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        todo = Todo.objects.get(id=id)
        todo.delete()
        data = {
            "message": "Todo succesfully deleted."
        }
        return Response(data, status=status.HTTP_204_NO_CONTENT)'''
#! GENERİC API Views
#class TodoList(mixins.ListModelMixin, mixins.CreateModelMixin, GenericAPIView):
#    queryset=Todo.objects.all()
#    serializer_class=TodoSerializer
#
#    def get(self, request, *args, **kwargs):   #! get listelemek için
#        return self.list(request, *args, **kwargs)
#    
#    def post(self, request, *args, **kwargs):   #! post listelemek için class bölümüne mixins.cretaeModelMixin'i ekle
#            return self.create(request, *args, **kwargs)
 #!CONCRETE VİEW CLASSES 
#class TodoListCreate(ListCreateAPIView):
#    queryset=Todo.objects.all()
#    serializer_class=TodoSerializer
#
#class TodoGetUpdateDelete(RetrieveUpdateDestroyAPIView): #!doğrudan ctrl+soltık ile kaynağı görüp işime yarayanı bulup yazdım
#    queryset=Todo.objects.all()
#    serializer_class=TodoSerializer
#    lookup_field='id'  #! alanı seçmek, id kullanmak için

class TodoMVS(viewsets.ModelViewSet):
    queryset=Todo.objects.all()
    serializer_class=TodoSerializer

    @action(methods=["GET"], detail=False)
    def todo_count(self, request):
        todo_count=Todo.objects.filter(done=False).count()
        count={
            "undo-todos":todo_count
        }
        return Response(count)    #!done olamyanları saydık.

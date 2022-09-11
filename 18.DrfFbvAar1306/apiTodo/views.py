from django.http.response import HttpResponse
from django.shortcuts import render

from .serializers import TodoSerializer
from rest_framework import status


# Create your views here.
def home(request):
    return HttpResponse(
        '<center><h1 style="background-color:powderblue;">Welcome to ApiTodo</h1></center>'
    )

from rest_framework.decorators import api_view #! hangi paket niçin çağrıldı göstermek için buraya yazıldı.
from rest_framework.response import Response
from .models import Todo
from .serializers import TodoSerializer

@api_view()  #! functionbase view def ile başlar, rest fw olduğunun anlaşılamsı için @api konur.
def hello_world(request):
    return Response ({"message": "Hello, world!"})


#! şimdi todo modelimize göre göstermek istediklerim için bir views yazıyorum.
@api_view(['GET']) #! ne amaçla kullanılacaksa parantez içine yazılır.
def todoList(request):
    queryset= Todo.objects.all() #! bütün todo objelerini bir queryset adındaki değişkene atadım.
    print('queryset')  #! kelimeyi yazdı
    print(queryset)     #! objeyi yazdı

    serializer=TodoSerializer(queryset,many=True)  #! views içine döüştürülmesini beklediğim  (serializerdeki)verileri bir değişkene atıyarak koyuyorum, çok sayıda olduğu için many0true koydum.
    print("serializer")    #! kelimeyi yazdı
    print(serializer)      #! obje içeriğini yazdıiçeriği yazdı
    
    return Response(serializer.data)  #!response olarak  serializer dönüştürülen verileri döndürüyorum

@api_view ( ['POST'] )  #! DİKKAT OFFİCE'DEN KOPYALANAN KOD İÇİNDEKİ KESME İŞARETLERİ UYUMUSZ İKAZ EDERSE KESMELERİ YENİDEN YAZ.
def todoCreate(request): #! views eklendiği gibi def'ler de url'ye eklenmeli
    serializer=TodoSerializer(data=request.data) #! data=request.data denmezse hata verir.

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data ) #! return'de bir özellik var açıklanacak, böyle çalışıyor.

#! iki fonksiyonu birleştirerek GET & POST'u beraber yapmak.

@api_view(['GET', 'POST'])
def todoListCreate(request):
    if request.method=='GET':
        querset=Todo.objects.all()
        serializer=TodoSerializer(querset, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK ) #! dökümantasyon açıklaması, formay bu
    
    elif request.method=='POST':
        serializer=TodoSerializer(data=request.data)

        if serializer.is_valid(): #!--valid için field özelliklerine baktı
            serializer.save()
            return Response (serializer.data, status=status.HTTP_201_CREATED)  #! return if hizasında olmayınca alt satıra geçmiyor.

    return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view([ 'GET', 'PUT'])
def todoUpdate(request, pk):
    querset = Todo.objects.get(id = pk)
    if request.method=='GET':
        serializer = TodoSerializer(querset)
        return Response(serializer.data)

    elif request.method=='PUT':
        serializer=TodoSerializer(instance=querset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response (serializer.data, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_204_NO_CONTENT)

@api_view(['DELETE'])
def todoDelete(request, pk):
    querset = Todo.objects.get(id = pk)
    querset.delete()
    return Response('selected item is deleted')
#! browser'dan id ile çağrılınca get bu işlemi yapmaz diyor ancak "DELETE " işlemi çıkıyor bu butonla işlem yürüyor.
#! 7 numaralı eleman silindi.

#! ----ÜÇ FONKSİYONLARIN BİRLEŞTİRİLMESİ----
@api_view([ 'GET', 'PUT', 'DELETE'])
def todoUpdate(request, pk):
    querset = Todo.objects.get(id = pk)
    if request.method=='GET':
        serializer = TodoSerializer(querset)
        return Response(serializer.data)

    elif request.method=='PUT':
        serializer=TodoSerializer(instance=querset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response (serializer.data, status=status.HTTP_201_CREATED)
    
        return Response(serializer.errors, status=status.HTTP_204_NO_CONTENT)

    elif request.method=='DELETE':
        querset.delete()
        return Response('selected item is deleted')

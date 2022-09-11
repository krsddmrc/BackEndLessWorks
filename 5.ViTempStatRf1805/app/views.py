from django.shortcuts import render
from django.http import HttpResponse


def home(request):      # aslında bir fonksiyon yazdık, parentez içine herzaman bir request alır.
    print(request.META) #
    return HttpResponse('<h1>Hello Class!</h1>') #Buraya {{request.user}} yazınca cevap alamadım.
                                                # istediğimi yazdırabilmek için ek ihtiyaçlar oluyor.
                                                #! bunun için bir  html sayfası hazırlayıp onu render ediyorum.
def special(request):       # bir html sayfası yazdım, retrun içerisinde request ile çağırdım
    context = {
        'title': 'clarusway',
        'dict1': {'django': 'best framework'},
        'my_list': [2, 3, 4]
    }    
    return render(request, 'app/special.html', context) #! python render ederken "template sayfası arıyor."
    #! template hatalı yazılmamalı,ayrıca template altına app ile aynı isimli bir klasör olmalı öge ve buraya yerleştirilmeli.
    #! Template altında yani django ortamında yazmak için bahsi geçen şekildeki ifadeleri kullanıyoruz.
    #! bir context (html'ye) eklemek istersem yerlerine dikkat
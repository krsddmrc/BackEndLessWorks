from weatherapp.models import City
from django.shortcuts import get_object_or_404, redirect, render
from decouple import config
import requests
from pprint import pprint
from django.contrib import messages


def home(request):
    API_key = config('API_KEY')
    u_city = request.GET.get('name') #! 1.GET-metod, 2.get-- getting data, u_city--user's city
    #! API'den çekip Database'e kayıt
    if u_city:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={u_city}&appid={API_key}&units=metric"
        response = requests.get(url) #!---response oluşturuyoruz, url’yi yukardan alıyor, veri şuan json.
        if response.ok: #! iif it is under 400
            content = response.json()#!content (isim değişebilir) içeriği artık bir python dictionary’e  dönüştü. 
            #pprint(content) #! ---ilk kontrol için çeklen veriler
            # #pprint(content['name'])
            #pprint(content['main']['temp'])
            #pprint(content['main']['temp'])  
            #pprint(content['weather'][0]['description'])
            #pprint(content['weather'][0]['icon'])
            r_city = content['name']
            if City.objects.filter(name=r_city):
                pprint(content)
                messages.warning(request, 'City already exists!')
            else:
                City.objects.create(name=r_city)
                messages.success(request, 'City created!')
        else:
            messages.error(request, 'There is no city!')
        return redirect('home')
    #! Database'den front-end'te gösterim
    city_data = []
    cities = City.objects.all()
    for city in cities:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_key}&units=metric"
        response = requests.get(url)
        content = response.json()
        data = {
            # 'city': content['name'],
            'city': city, #! content içierisnde ıp'den gelen city "id"si yok, bu yüzen city'i döngü içindeki "city" objesine eşitledim, ototmatik oluşturduğu "id" kullandı.
            'temp': content['main']['temp'],
            'icon' : content['weather'][0]['icon'],
            'desc' : content['weather'][0]['description'],
        }
        city_data.append(data)
        
    context = {
        'city_data': city_data,
    }
    return render(request, 'weatherapp/home.html', context)

def delete_city(request, id):
    city = get_object_or_404(City, id=id)
    city.delete()
    messages.success(request, 'City deleted!')
    return redirect('home')  #! son girilen bilgilerden veri kalmaması için  başlangıca dönmesini sağladık.
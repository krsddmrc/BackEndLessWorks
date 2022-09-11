from django.urls import path
from .views import home, special

urlpatterns = [
    path('', home, name='home'), # '' ile bu app.urls de 'home'a geldik, sonra ne yazıldı ise buradan dağıtılacak.
    path('special', special, name='special') 
]
#name  link olarak kullanılabiliyor.
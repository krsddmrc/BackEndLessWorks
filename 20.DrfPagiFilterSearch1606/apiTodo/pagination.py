from rest_framework import pagination
#from rest_framework.pagination import PageNumberPagination #! ikinci usul

#class MyPageNumberPagination(PageNumberPagination):#! ikinci usulde

class SmallPageNumberPagination(pagination.PageNumberPagination): #! iki ayrı isim (class) oluşturdum.
    page_size=1
    page_query_param='sayfa'  #!page yazısını sayfa yatım, daha az içerik taşıyor.

class LargePageNumberPagination(pagination.PageNumberPagination): 
    page_size=3
    # page_query_param='sayfa' #!page olarak kaldı, daha fazla içerik taşıyor.

class MyLimitOffsetPagination(pagination.LimitOffsetPagination): #! class ismi serbest ancak, metod ismi ile aynı olmamalı
    default_limit=2
    limit_query_param="SES"   #!requette yazarken hata yapsa default görünür
    offset_query_param="baslangic" #!defaults to offset

class MyCursorPagination(pagination.CursorPagination):
    ordering="createdDate"
    page_size=2
from django.contrib import admin
from .models import Product
from django.utils import timezone

class ProductAdmin(admin.ModelAdmin): #! parantez içine ctrl+sol click değiştirilebilecek attr. çıkarır
    #! list_display=("__str__",) (admin.ModelAdmin) ifadesinin içeriğini değiştirdim.
    list_display = ("name", "create_date", "is_in_stock", "update_date")
    list_editable = ( "is_in_stock", )  #! Liste sayfasından  işleme alabilmek için, link varasa olmuyor 
    list_display_links = ("name", "create_date", ) #! link name'de başka değişkene link eklemek veya değiştirmek için, ayrıntıya gider.
    list_filter = ("is_in_stock", "create_date") #! filtrelenecek alanlar açılıyor,
    ordering = ("name",)  #! düzenleme alanı
    search_fields = ("name",) #! arama alanı, default küçük büyük harf duyayrlı değil.
    prepopulated_fields = {'slug' : ('name',)} 
    list_per_page = 25 #! sayfada nekadar sayıda gösterileceği
    date_hierarchy = "update_date"  #! tarih sıarlamasını neye göre yapacağı
    #fields = (('name', 'slug'), 'description', "is_in_stock") #!fieldset kullandığımız zaman bunu kullanamayız
    #!field ve field set admin panelde görüneceklerin kümelenmesi ve gösterilmesi ile ilgili
    fieldsets = (
        (None, {
            "fields": (# to display multiple fields on the same line, wrap those fields in their own tüple),
                ('name', 'slug'), "is_in_stock"
            ), 
            #'classes': ('wide', 'extrapretty'), wide or collapse
    }),
	('Optionals Settings', {
            "classes": ("collapse", ),
            "fields": ("description", "categories", "product_img", "bring_image"),
            'description': "You can use this section for optionals settings"
    })
)

actions = ("is_in_stock", )  #!actions tanımladım ve tanıma is_in_stock yerleştirdim.
filter_horizontal = ("categories", )

def is_in_stock(self, request, queryset):  #! seçenekleri bir queryset olarak hazırlıyor.
    count = queryset.update(is_in_stock=True) #! query set içine girenleri topluca stokta True yapıyor.
    self.message_user(request, f"{count} products added to stock.")

is_in_stock.short_description = 'add to stock' #! "is_in_stock" "add to stock" olarak değişti.

def added_days_ago(self, product): #!modelimizde olmayan bir alan, ürünün kaçgün önce eklendiğini göstermek için ekledik.
    days = timezone.now() - product.create_date #! timezone import edilmeli
    return days.days

admin.site.register(Product, ProductAdmin) #! product model değiştiğinden  görebilmem için register gerekli
# Register your models here.
admin.site.site_title = "Clarusway Title"
admin.site.site_header = "Clarusway Admin Portal"  
admin.site.index_title = "Welcome to Clarusway Admin Portal"
from django.db import models  
    
class Path (models.Model): #! class students altına path ekledim ve bu model ilişkilendirildiği için sqlite db sildim,  
    path_name=models.CharField(max_length=10)  #! ayrıca migrations içinde 0001 ve 0002'yi sildim.
                                                #! superuser'da gitti, silinince , yeniden migrations yapılmalı
    def __str__(self):
        return self.path_name

class Student(models.Model): 
    path=models.ForeignKey(Path, related_name='students', on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30) 
    last_name = models.CharField(max_length=30) 
    number = models.IntegerField(null=True)
    register_date=models.DateTimeField(auto_now_add=True) #! migrations yapınca önceki kayıtlar ile ilgili girdi istedi.

    def __str__(self):
        return self.first_name

	# blank=True for admin dashboard 
	# null=True for db def __str__(self): return f"{self.last_name} {self.first_name}"

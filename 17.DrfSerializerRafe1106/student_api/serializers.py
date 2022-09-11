
from pyexpat import model
from rest_framework import serializers
from .models import Path, Student
from django.utils.timezone import now

#class StudentSerializer(serializers.Serializer):    #!döküman  API guide- saving instance bölümünden 
#    first_name = serializers.CharField(max_length=30)     #! alt başlıkları modelimden aldım, models'leri serializers yaptım
#    last_name = serializers.CharField(max_length=30) 
#    number = serializers.IntegerField()
#    #id=serializers.IntegerField() #! ben ekledim. refresh yapınca göründü, id sqlite 'dan geliyor.
#                                #! modelde olanları ekleyebiliriz
#    def create(self, validated_data):
#            return Student.objects.create(**validated_data)
#
#    def update(self, instance, validated_data):
#           instance.first_name= validated_data.get('first_name', instance.first_name)
#           instance.lastname = validated_data.get('lastname', instance.last_name)
#           instance.number = validated_data.get('number', instance.number)
#           instance.save()
#           return instance

class StudentSerializer(serializers.ModelSerializer): #! Student modelinden al dedim ve hangi field'ları istiyorsam bildirdim.
    days_since_joined=serializers.SerializerMethodField()
    class Meta:
        model = Student
        #fields = ['id', 'first_name', 'last_name', 'number', 'days_since_joined'] #! hepsi için "__all__" denebilirdi.
        fields = '__all__'
        # exclude=['id']

    def validate_number(self,value):
        if value > 1000:
            raise serializers.ValidationError("Number must below 1000!")
        return value

    def validate_first_name(self,value):
        if value.lower() == 'rafe':
            raise serializers.ValidationError("Rafe can not be student!")
        return value 

    def get_days_since_joined(self, obj):
        return(now()-obj.register_date).days         
        #return(now()-obj.register_date).seconds      #! saniye olarak   
    
class PathSerializer(serializers.ModelSerializer):
    #students=StudentSerializer (many=True) #! birden fazla öğrenci geleceği için many=True olmalı
    #                                        #! path ler altına student'tan verileri çekti.
    #students=serializers.StringRelatedField (many=True) #!Farkı, model str'da tanımladığımız alanlar geldi
    students=serializers.PrimaryKeyRelatedField (read_only=True, many=True) #!Farkı, öğrencileri id'lerini yazdı.
    class Meta:
        model=Path
        fields='__all__'

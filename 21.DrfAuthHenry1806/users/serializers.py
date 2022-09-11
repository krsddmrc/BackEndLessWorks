from wsgiref.validate import validator
from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password

class RegisterSerializer(serializers.ModelSerializer):
        email=serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=User.objects.all())] #!emailField uniqe hale geldi aynı email girişi yapana default hata dönecek
        )

        password=serializers.CharField(
            write_only=True,    #! post işleminde göndereyim, response data ile geri dönmesin."""read_only=True   get işleminde okunsun ancak post işleminde bu field'i kullanma demek"""
            required=True,
            validators=[validate_password], #! birini validate etmek yeterli
            style={
                'input_type':'password'
            }
        )

        password2=serializers.CharField(
            write_only=True,    #! post işleminde göndereyim, response data ile geri dönmesin. 
            required=True,
            style={
                'input_type':'password'
            }
        )

        class Meta:
            model=User
            fields=(
                'username',
                'email',
                'first_name',
                'last_name',
                'password',
                'password2'
            )
        def validate(self,attrs):  #! email alanları için bir validate yazdım.
            if attrs['password']!=attrs['password2']:
                raise serializers.ValidationError(
                    {'password': 'Password fields did not match' }
                )
            return attrs

        def create(self, validated_data): #! validated data- bir dictionary yapısında gelen bir veriydi.
            validated_data.pop('password2')
            password=validated_data.pop('password') #! POP İLE ÇIAKRDIM BAŞKA BİR DEĞİŞKENE ATADIM
            user=User.objects.create(**validated_data)
            user.set_password(password) #! bunun maksdı hashlemesi 
            user.save()
            return user


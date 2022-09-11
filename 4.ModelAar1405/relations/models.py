from tkinter import CASCADE
from django.db import models

class Creator(models.Model):       #! main table
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)

    def __str__(self):
        return self.first_name

class Language(models.Model):   #! a subject in main table have one to one relatoins
    name=models.CharField(max_length=20) #! A person, in main table can get only one language
    producer=models.OneToOneField(Creator, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Framework(models.Model): #! a subject in Language table in one to many relatoins
    name=models.CharField(max_length=30) #! A Languge, in table can get some of frameworks
    language=models.ForeignKey(Language, on_delete=models.PROTECT)

    def __str__(self):
        return self.name

class Developer(models.Model): #! every subject in framework table have many to many relatoins
    name=models.CharField(max_length=30) #! Every developer, in table can get every frameworks
    last_name=models.CharField(max_length=30)
    framework=models.ManyToManyField(Framework)

    def __str__(self):
        return f'{self.name}{self.last_name}'


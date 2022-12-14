from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    portfolio = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)


    username=models.EmailField('Email Address', unique=True)
    REQUIRED_FIELDS=[] #! username'i emaile bağladım ve unıqu yaptım.
    #! formdan emaili silmezzsem iki tane görükür, bu yüzden formda siliyorum.

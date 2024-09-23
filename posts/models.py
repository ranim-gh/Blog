from django.db import models
from datetime import datetime
from datetime import date




# Create your models here
class Post(models.Model): 
    
    title = models.CharField(max_length=50)
    
    body =  models.CharField(max_length=100000)

    time = models.DateTimeField(default=datetime.now, blank=True)
    

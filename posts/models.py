from django.db import models
from datetime import datetime



# Create your models here
class Post(models.Model): 
    
    title = models.CharField(max_length=50)
    
    body =  models.CharField(max_length=100000)

    time = models.TimeField(default=datetime.now, blank= True )

    

from django.contrib import admin
from .models import Post 

# Register your models here.

print(Post) 
admin.site.register(Post)

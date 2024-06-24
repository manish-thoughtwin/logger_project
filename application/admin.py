from django.contrib import admin
from .models import Registration

# Register your models here.


class RegistrationnAdmin(admin.ModelAdmin):
  list_display = ("first_name","last_name","email")
  
admin.site.register(Registration, RegistrationnAdmin)   
  
  



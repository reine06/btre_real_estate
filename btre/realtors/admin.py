from django.contrib import admin
from .models import Realtor

# Register your models here.
# admin.site.register(Realtor)

@admin.register(Realtor)
class RealtorAdmin(admin.ModelAdmin):
      list_display=('id','name','email','hire_date')
      list_per_page=('id','name')
      search_fields=('name',)
      list_per_page=20
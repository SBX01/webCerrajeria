from django.contrib import admin
from .models import Servicio,agendaServicio
# Register your models here.

class Agenda(admin.ModelAdmin):
  list_display=['nombre','tipoServicio']
  search_fields=['nombre']
  list_filter=['tipoServicio']
  list_per_page =15
  
admin.site.register(Servicio)
admin.site.register(agendaServicio, Agenda)


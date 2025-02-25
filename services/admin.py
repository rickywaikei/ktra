from django.contrib import admin
from .models import Service

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('id','service_type','title','location','instructor', 'photo_main', 'photo_1', 'service_start_time','service_end_time')
    list_display_links = ('id','title')
    list_filter = 'service_type','service_start_time'
    search_fields = 'title','content'
    list_per_page = 20
    
admin.site.register(Service,ServiceAdmin)
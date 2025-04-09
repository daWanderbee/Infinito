# Register your models here.
from django.contrib import admin
from .models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'registration_number', 'vit_email', 'hostel', 'room_number', 'game_playing')
    search_fields = ('name', 'registration_number', 'vit_email', 'hostel', 'game_playing')
    list_filter = ('hostel', 'game_playing')


admin.site.site_header = "VIT Sports Registration"
admin.site.site_title = "VIT Admin Portal"
admin.site.index_title = "Welcome to VIT Sports Dashboard"

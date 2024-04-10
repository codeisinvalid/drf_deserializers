from django.contrib import admin
from .models import Student

class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'grade', 'roll', 'city')

# Register your models here.
admin.site.register(Student, StudentAdmin)

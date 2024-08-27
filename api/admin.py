from django.contrib import admin
from .models import Student
@admin.register(Student)
class Student_admin(admin.ModelAdmin):
    list_display=['id','name','age','city']


# Register your models here.

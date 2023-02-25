from django.contrib import admin
from .models import students

@admin.register(students)
class adminstudents(admin.ModelAdmin):
    list_display=['id','name','roll','cp']

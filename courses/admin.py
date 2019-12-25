from django.contrib import admin
from .models import offerings

# Register your models here.
class MainCourse(admin.ModelAdmin):
    list_display = ('course_title', 'course_slug', 'course_status','course_created_on')
    list_filter = ("course_status",)
    search_fields = ['course_title', 'course_name']
    prepopulated_fields = {'course_slug': ('course_title',)}

admin.site.register(offerings,MainCourse)
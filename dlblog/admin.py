from django.contrib import admin
from .models import Blog,UseCase,Comment


# Register your models here.



class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status','created_on')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Blog,BlogAdmin)

class UseCaseAdmin(admin.ModelAdmin):
    list_display = ('usecase_title', 'usecase_slug', 'usecase_status','usecase_created_on')
    list_filter = ("usecase_status",)
    search_fields = ['usecase_title', 'usecase_content']
    prepopulated_fields = {'usecase_slug': ('usecase_title',)}

admin.site.register(UseCase,UseCaseAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)


from django.contrib import admin

# Register your models here.
from blog import models

class PostAdmin(admin.ModelAdmin):
	list_display=('title', 'created_time', 'modified_time')
	search_fields=('author',)
	ordering = ('-created_time', )

admin.site.register(models.Post, PostAdmin)

admin.site.register(models.Tag)
admin.site.register(models.Category)

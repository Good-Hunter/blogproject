from django.contrib import admin

# Register your models here.
from comments import models

class CommentAdmin(admin.ModelAdmin):
	list_display=('name','email','post', 'created_time')
	search_fields=('post',)
	ordering = ('-created_time', )

admin.site.register(models.Comment, CommentAdmin)



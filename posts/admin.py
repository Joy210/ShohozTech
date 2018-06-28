from django.contrib import admin

# App Model
from .models import Post


class PostAdmin(admin.ModelAdmin):
    """Customizing Admin Interface"""
    list_display = ['id', 'title', 'updated', 'timestamp',  'content']
    list_display_links = ['updated']
    list_filter = ['updated', 'timestamp']
    list_editable = ['title']
    search_fields = ['title', 'content']


# Register the custom Admins
admin.site.register(Post, PostAdmin)




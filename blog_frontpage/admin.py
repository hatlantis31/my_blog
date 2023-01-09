from django.contrib import admin

from blog_frontpage.models import Post


# Register your models here.
@admin.register(Post)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_on', 'author', 'status')  # fields to display in the admin list view
    list_filter = ('created_on', 'author')  # fields to filter by in the admin list view
    search_fields = ('title', 'body')  # fields to search by in the admin list view
    prepopulated_fields = {'slug': ('title',)}  # fields to prepopulate in the admin add view
    raw_id_fields = ('author',)  # fields to display as a raw id in the admin add view
    date_hierarchy = 'created_on'  # date hierarchy to display in the admin list view
    ordering = ('created_on',)  # default ordering for the admin list view

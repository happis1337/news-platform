from django.contrib import admin
from django.contrib.auth.models import User, Group

from .models import *

admin.site.unregister(Group)
admin.site.unregister(User)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


class ContentInline(admin.StackedInline):
    model = Content
    extra = 1


class CommentInline(admin.StackedInline):
    model = Comment
    extra = 0


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'reading_time', 'category', 'views', 'comments', 'published')
    search_fields = ('title', 'category__name', 'tags__name')
    list_filter = ('category', 'published', 'tags')
    inlines = [ContentInline, CommentInline]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'email', 'created_at', 'article')
    search_fields = ('author', 'text',)
    list_filter = ('author', 'article')


@admin.register(NewsLetter)
class NewsletterAdmin(admin.ModelAdmin):
    list_display = ('email',)
    search_fields = ('email',)


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'subject', 'phone_number', 'message')
    search_fields = ('full_name', 'email', 'subject', 'phone_number', 'message')
    list_filter = ('subject', 'phone_number', 'subject')


@admin.register(Gallary)
class GallaryAdmin(admin.ModelAdmin):
    list_display = ('created_at',)
    search_fields = ('created_at',)
    list_filter = ('created_at',)
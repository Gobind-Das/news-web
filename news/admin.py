from django.contrib import admin
from django.utils.html import format_html
from .models import Category, Article


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'order', 'article_count')
    prepopulated_fields = {'slug': ('name',)}
    ordering = ('order', 'name')

    def article_count(self, obj):
        return obj.articles.count()

    article_count.short_description = 'Articles'


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'author', 'status_badge', 'published_at', 'views')
    list_filter = ('status', 'category', 'created_at', 'published_at')
    search_fields = ('title', 'slug', 'summary')

    # ✅ Slug auto-generated from title
    prepopulated_fields = {'slug': ('title',)}

    # ❌ DO NOT put slug here (this caused your error)
    readonly_fields = ('views', 'created_at', 'updated_at')

    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'slug', 'category', 'author')
        }),
        ('Content', {
            'fields': ('summary', 'content', 'featured_image')
        }),
        ('Publishing', {
            'fields': ('status', 'published_at')
        }),
        ('SEO', {
            'fields': ('meta_title', 'meta_description', 'meta_keywords'),
            'classes': ('collapse',)
        }),
        ('Stats', {
            'fields': ('views', 'created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

    def status_badge(self, obj):
        colors = {
            'draft': '#FFA500',
            'published': '#28a745',
            'archived': '#6c757d'
        }
        return format_html(
            '<span style="background-color: {}; color: white; padding: 5px 10px; border-radius: 3px;">{}</span>',
            colors.get(obj.status, '#000000'),
            obj.get_status_display()
        )

    status_badge.short_description = 'Status'

    def save_model(self, request, obj, form, change):
        if not change:
            obj.author = request.user
        super().save_model(request, obj, form, change)

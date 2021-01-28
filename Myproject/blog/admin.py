from django.contrib import admin
from .models import Article, Category

# Admin header change
admin.site.site_header = "وبلاگ"


# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('position', 'title', 'slug', 'parent', 'status')
    list_filter = (['status'])
    search_fields = ('title', 'slug')
    prepopulated_fields = {'slug': ('title',)}
    actions = ['make_active', 'make_disable']
    
    def make_active(self, request, queryset):
        rows_update = queryset.update(status = True)
        if rows_update == 1:
            message_bit = "فعال شد"
        else:
            message_bit = "فعال شدند"
        self.message_user(request, "{} دسته بندی {}".format(rows_update, message_bit))
    make_active.short_description = "فعال کردن دسته بندی های انتخاب شده"
    
    def make_disable(self, request, queryset):
        rows_update = queryset.update(status = False)
        if rows_update == 1:
            message_bit = "غیر فعال شد"
        else:
            message_bit = "غیر فعال شدند"
        self.message_user(request, "{} دسته بندی {}".format(rows_update, message_bit))
    make_disable.short_description = "غیر فعال کردن دسته بندی های انتخاب شده"

admin.site.register(Category, CategoryAdmin)

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'thumbnail_tag', 'slug', 'jpublish', 'status', 'category_to_str')
    list_filter = ('publish', 'status')
    search_fields = ('title', 'description')
    prepopulated_fields = {'slug': ('title',)}
    ordering = ['-status', '-publish']
    actions = ['make_published', 'make_draft']

    def category_to_str(self, obj):
        return ", ".join([category.title for category in obj.category.active()])
    category_to_str.short_description = "دسته بندی"
    
    def make_published(self, request, queryset):
        rows_update = queryset.update(status = 'p')
        if rows_update == 1:
            message_bit = "منتشر شد."
        else:
            message_bit = "منتشر شدند"
        self.message_user(request, "{} مقاله {}".format(rows_update, message_bit))
    make_published.short_description = "انتشار مقالات انتخاب شده"
    
    def make_draft(self, request, queryset):
        rows_update = queryset.update(status = 'd')
        if rows_update == 1:
            message_bit = "پیش نویس شد"
        else:
            message_bit = "پیش نویس شدند"
        self.message_user(request, "{} مقاله {}".format(rows_update, message_bit))
    make_draft.short_description = "پیش نویس شدن مقالات انتخاب شده"
    
admin.site.register(Article, ArticleAdmin)
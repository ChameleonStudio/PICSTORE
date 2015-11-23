from django.contrib import admin
from core.models import Category, Picture, Sale, Tag, SuperCategory


class TagInline(admin.TabularInline):
    model = Picture.tags.through
    extra = 0


class PictureAdmin(admin.ModelAdmin):
    inlines = [TagInline]
    fields = ('picture', 'name', 'short_description', 'price', 'category', 'sale')
    list_display = ('display_thumbnail', 'name', 'category', 'price', 'created', 'sale', 'tag_list')
    list_editable = ('name', 'sale')
    list_filter = ('category', )
    search_fields = ('name', 'short_description', 'category', 'tags')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'super_category', 'display_icon')
    list_editable = ('super_category', )


class TagAdmin(admin.ModelAdmin):
    list_display = ('name', )
    list_editable = ('name', )


admin.site.register(Category, CategoryAdmin)
admin.site.register(SuperCategory)
admin.site.register(Picture, PictureAdmin)
admin.site.register(Sale)
admin.site.register(Tag, TagAdmin)

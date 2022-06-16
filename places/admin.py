from django.contrib import admin
from .models import Place, PlaceImage
from django.utils.html import format_html
from adminsortable2.admin import SortableAdminBase, SortableInlineAdminMixin


class PlaceImageInline(SortableInlineAdminMixin, admin.TabularInline):
    model = PlaceImage
    extra = 0
    readonly_fields = (
        'img_preview',
    )
    fields = ('image', 'img_preview')

    def img_preview(self, instance):
        return format_html('<img src="{url}" height="{height}" />',
            url = instance.image.url,
            height="200px",
        )



@admin.register(Place)
class PlaceAdmin(SortableAdminBase, admin.ModelAdmin):
    search_fields = ('title',)
    inlines = [
        PlaceImageInline,
    ]

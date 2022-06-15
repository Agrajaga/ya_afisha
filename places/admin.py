from django.contrib import admin
from .models import Place, PlaceImage
from django.utils.html import format_html


class PlaceImageInline(admin.TabularInline):
    model = PlaceImage
    readonly_fields = (
        'img_preview',
    )
    fields = ('image', 'img_preview', 'index')

    def img_preview(self, instance):
        return format_html('<img src="{url}" height="{height}" />',
            url = instance.image.url,
            height="200px",
        )



@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = [
        PlaceImageInline,
    ]

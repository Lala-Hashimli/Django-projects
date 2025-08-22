from django.contrib import admin
from django.utils.html import format_html
from .models import Flowers, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name",)
    search_fields = ("name",)


@admin.register(Flowers)
class FlowersAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "category",
        "color",
        "quantity",
        "price_before_discount",
        "price_after_discount",
        "image",
        "raiting",
        "show_raiting_stars",
        "status",
        "created_at",
        "updated_at",
        "expires_at_display"
    )
    list_filter = ("category", "color", "raiting", "status", "created_at",)
    search_fields = ("title", "description")
    readonly_fields = ("created_at", "updated_at", "expires_at")
    list_editable = ("status","image",)


    def show_raiting_stars(self, obj):
        return obj.raiting_stars
    show_raiting_stars.short_description = "Rating Stars"

  
    def expires_at_display(self, obj):
            from django.utils import timezone
            from django.utils.html import format_html

            if obj.expires_at:
                now = timezone.now()
                if obj.expires_at < now:
                    return format_html('<span style="color:red;">{}</span>', obj.expires_at.strftime("%Y-%m-%d %H:%M"))
                return obj.expires_at.strftime("%Y-%m-%d %H:%M")
            return "-"
        
    expires_at_display.short_description = "Expires At"
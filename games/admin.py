from django.contrib import admin

from .models import *


class GameGenreInline(admin.TabularInline):
    model = GameGenre
    extra = 1


class GameTagInline(admin.TabularInline):
    model = GameTag
    extra = 1


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    inlines = [GameGenreInline, GameTagInline]
    readonly_fields = ["created_date"]
    list_display = ["name"]
    fieldsets = [
        (
            "info",
            {
                "fields": [
                    "category", "name", "caption",
                    "description", "price", "discount_percent",
                    "game_id", "is_active", "most_played",
                    "is_trending", "created_date",
                ],
            },
        ),
        (
            "images",
            {
                "fields": ["detail_image", "image", "most_played_image", "most_discounted_image"],
            },
        ),
    ]


@admin.register(Genre)
class GenerAdmin(admin.ModelAdmin):
    fields = ["name", "created_date"]
    readonly_fields = ["created_date"]
    list_display = ["name"]


@admin.register(Tag)
class GenerAdmin(admin.ModelAdmin):
    fields = ["name", "created_date"]
    readonly_fields = ["created_date"]
    list_display = ["name"]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    fields = ["name", "caption", "is_top", "image", "created_date"]
    readonly_fields = ["created_date"]
    list_display = ["name", "caption"]
    list_display_links = ["name", "caption"]

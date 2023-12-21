from django.contrib import admin

from .models import Feature


@admin.register(Feature)
class FeatureAdmin(admin.ModelAdmin):
    fields = ["name", "logo"]
    list_display = ["name"]

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        if self.model.objects.count() <= 3:
            return super().has_add_permission(request)
        return False

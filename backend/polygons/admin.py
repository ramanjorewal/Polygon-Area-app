"""
Admin configuration for Polygon model.
"""
from django.contrib import admin
from .models import Polygon


@admin.register(Polygon)
class PolygonAdmin(admin.ModelAdmin):
    """
    Admin interface for Polygon model.
    """
    list_display = ('name', 'area_sq_meters', 'perimeter_meters', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('name',)
    readonly_fields = ('area_sq_meters', 'perimeter_meters', 'created_at', 'updated_at')
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'coordinates')
        }),
        ('Calculated Metrics', {
            'fields': ('area_sq_meters', 'perimeter_meters'),
            'classes': ('collapse',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    def has_add_permission(self, request):
        """Allow adding polygons through admin."""
        return True
    
    def has_change_permission(self, request, obj=None):
        """Allow editing polygons through admin."""
        return True
    
    def has_delete_permission(self, request, obj=None):
        """Allow deleting polygons through admin."""
        return True 
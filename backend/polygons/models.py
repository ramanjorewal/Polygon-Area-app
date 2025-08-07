from django.db import models
from django.core.validators import MinValueValidator
from decimal import Decimal
import json
from shapely.geometry import Polygon as ShapelyPolygon
from shapely.geometry import MultiPolygon as ShapelyMultiPolygon


class Polygon(models.Model):
    name = models.CharField(max_length=255, blank=True)
    coordinates = models.JSONField(help_text="List of coordinate pairs [[lng, lat], ...]")
    area_sq_meters = models.DecimalField(
        max_digits=15, 
        decimal_places=2, 
        validators=[MinValueValidator(Decimal('0.01'))],
        help_text="Area in square meters"
    )
    perimeter_meters = models.DecimalField(
        max_digits=15, 
        decimal_places=2, 
        validators=[MinValueValidator(Decimal('0.01'))],
        help_text="Perimeter in meters"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Polygon"
        verbose_name_plural = "Polygons"

    def __str__(self):
        return f"{self.name or 'Unnamed'} - {self.area_sq_meters} m²"

    def calculate_metrics(self):
        if not self.coordinates or len(self.coordinates) < 3:
            raise ValueError("At least 3 coordinate pairs are required for a polygon")
        
        try:
            shapely_polygon = ShapelyPolygon(self.coordinates)
            
            if not shapely_polygon.is_valid:
                raise ValueError("Invalid polygon geometry")
            
            area_degrees = shapely_polygon.area
            self.area_sq_meters = Decimal(str(area_degrees * 111000 * 111000))
            
            perimeter_degrees = shapely_polygon.length
            self.perimeter_meters = Decimal(str(perimeter_degrees * 111000))
            
        except Exception as e:
            raise ValueError(f"Error calculating metrics: {str(e)}")

    def to_geojson(self):
        return {
            "type": "Feature",
            "geometry": {
                "type": "Polygon",
                "coordinates": [self.coordinates]
            },
            "properties": {
                "id": self.id,
                "name": self.name,
                "area_sq_meters": float(self.area_sq_meters),
                "perimeter_meters": float(self.perimeter_meters),
                "created_at": self.created_at.isoformat(),
                "updated_at": self.updated_at.isoformat()
            }
        }

    def save(self, *args, **kwargs):
        if self.coordinates:
            self.calculate_metrics()
        super().save(*args, **kwargs) 
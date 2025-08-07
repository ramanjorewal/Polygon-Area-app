from rest_framework import serializers
from .models import Polygon
from shapely.geometry import Polygon as ShapelyPolygon
from decimal import Decimal


class PolygonSerializer(serializers.ModelSerializer):
    area_hectares = serializers.SerializerMethodField()
    area_acres = serializers.SerializerMethodField()
    
    class Meta:
        model = Polygon
        fields = [
            'id', 'name', 'coordinates', 'area_sq_meters', 
            'perimeter_meters', 'area_hectares', 'area_acres',
            'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'area_sq_meters', 'perimeter_meters', 
                           'area_hectares', 'area_acres', 'created_at', 'updated_at']

    def get_area_hectares(self, obj):
        if obj.area_sq_meters:
            return float(obj.area_sq_meters) / 10000
        return None

    def get_area_acres(self, obj):
        if obj.area_sq_meters:
            return float(obj.area_sq_meters) / 4046.86
        return None

    def validate_coordinates(self, value):
        if not value or not isinstance(value, list):
            raise serializers.ValidationError("Coordinates must be a list of coordinate pairs")
        
        if len(value) < 3:
            raise serializers.ValidationError("At least 3 coordinate pairs are required for a polygon")
        
        for coord in value:
            if not isinstance(coord, list) or len(coord) != 2:
                raise serializers.ValidationError("Each coordinate must be a list with exactly 2 values [lng, lat]")
            
            lng, lat = coord
            if not isinstance(lng, (int, float)) or not isinstance(lat, (int, float)):
                raise serializers.ValidationError("Longitude and latitude must be numbers")
            
            if not (-180 <= lng <= 180):
                raise serializers.ValidationError("Longitude must be between -180 and 180")
            
            if not (-90 <= lat <= 90):
                raise serializers.ValidationError("Latitude must be between -90 and 90")
        
        try:
            shapely_polygon = ShapelyPolygon(value)
            if not shapely_polygon.is_valid:
                raise serializers.ValidationError("Invalid polygon geometry")
        except Exception as e:
            raise serializers.ValidationError(f"Invalid polygon: {str(e)}")
        
        return value


class PolygonListSerializer(serializers.ModelSerializer):
    area_hectares = serializers.SerializerMethodField()
    
    class Meta:
        model = Polygon
        fields = ['id', 'name', 'area_sq_meters', 'perimeter_meters', 
                 'area_hectares', 'created_at']
    
    def get_area_hectares(self, obj):
        if obj.area_sq_meters:
            return float(obj.area_sq_meters) / 10000
        return None 
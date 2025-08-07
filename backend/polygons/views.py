from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Polygon
from .serializers import PolygonSerializer, PolygonListSerializer


class PolygonViewSet(viewsets.ModelViewSet):
    queryset = Polygon.objects.all()
    serializer_class = PolygonSerializer

    def get_serializer_class(self):
        if self.action == 'list':
            return PolygonListSerializer
        return PolygonSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            polygon = serializer.save()
            return Response(
                serializer.data, 
                status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors, 
            status=status.HTTP_400_BAD_REQUEST
        )

    @action(detail=True, methods=['get'])
    def geojson(self, request, pk=None):
        polygon = self.get_object()
        geojson_data = polygon.to_geojson()
        return Response(geojson_data)

    @action(detail=False, methods=['get'])
    def geojson_collection(self, request):
        polygons = self.get_queryset()
        features = [polygon.to_geojson() for polygon in polygons]
        
        geojson_collection = {
            "type": "FeatureCollection",
            "features": features
        }
        
        return Response(geojson_collection)

    def destroy(self, request, *args, **kwargs):
        polygon = self.get_object()
        polygon.delete()
        return Response(
            {"message": "Polygon deleted successfully"}, 
            status=status.HTTP_204_NO_CONTENT
        ) 
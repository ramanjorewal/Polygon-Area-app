"""
URL patterns for polygon API endpoints.
"""
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PolygonViewSet

# Create router and register viewsets
router = DefaultRouter()
router.register(r'polygons', PolygonViewSet, basename='polygon')

urlpatterns = [
    path('', include(router.urls)),
] 
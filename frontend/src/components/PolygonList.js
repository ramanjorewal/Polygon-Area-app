import React, { useState, useEffect, useRef } from 'react';
import {
  Box,
  Grid,
  Card,
  CardContent,
  Typography,
  Button,
  Paper,
  Alert,
  CircularProgress,
  IconButton,
  Chip,
  Dialog,
  DialogTitle,
  DialogContent,
  DialogActions
} from '@mui/material';
import {
  Delete as DeleteIcon,
  Visibility as ViewIcon,
  Map as MapIcon,
  Refresh as RefreshIcon
} from '@mui/icons-material';
import { polygonAPI } from '../services/api';
import GoogleMap from './GoogleMap';

const PolygonList = () => {
  const [polygons, setPolygons] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');
  const [selectedPolygon, setSelectedPolygon] = useState(null);
  const [mapDialogOpen, setMapDialogOpen] = useState(false);
  const [map, setMap] = useState(null);
  const mapRef = useRef(null);

  useEffect(() => {
    loadPolygons();
  }, []);

  const loadPolygons = async () => {
    setLoading(true);
    setError('');
    
    try {
      const data = await polygonAPI.getAll();
      setPolygons(data.results || data);
    } catch (err) {
      setError('Failed to load polygons');
      console.error('Error loading polygons:', err);
    } finally {
      setLoading(false);
    }
  };

  const handleDelete = async (polygonId) => {
    if (!window.confirm('Are you sure you want to delete this polygon?')) {
      return;
    }

    try {
      await polygonAPI.delete(polygonId);
      setPolygons(polygons.filter(p => p.id !== polygonId));
    } catch (err) {
      setError('Failed to delete polygon');
      console.error('Error deleting polygon:', err);
    }
  };

  const handleViewOnMap = (polygon) => {
    setSelectedPolygon(polygon);
    setMapDialogOpen(true);
  };

  const initializeMapWithPolygon = (mapInstance) => {
    if (!selectedPolygon || !mapInstance) return;

    const coordinates = selectedPolygon.coordinates;
    const path = coordinates.map(coord => ({
      lat: coord[1],
      lng: coord[0]
    }));

    const polygon = new window.google.maps.Polygon({
      paths: path,
      fillColor: '#FF0000',
      fillOpacity: 0.3,
      strokeWeight: 2,
      strokeColor: '#FF0000',
      clickable: true,
      editable: false,
      zIndex: 1,
    });

    polygon.setMap(mapInstance);

    const bounds = new window.google.maps.LatLngBounds();
    coordinates.forEach(coord => {
      bounds.extend({ lat: coord[1], lng: coord[0] });
    });
    mapInstance.fitBounds(bounds);

    setMap(mapInstance);
  };

  const formatArea = (area) => {
    if (area < 10000) {
      return `${area.toFixed(2)} m²`;
    } else {
      const hectares = area / 10000;
      return `${hectares.toFixed(2)} ha (${area.toFixed(2)} m²)`;
    }
  };

  const formatPerimeter = (perimeter) => {
    if (perimeter < 1000) {
      return `${perimeter.toFixed(2)} m`;
    } else {
      const km = perimeter / 1000;
      return `${km.toFixed(2)} km (${perimeter.toFixed(2)} m)`;
    }
  };

  const formatDate = (dateString) => {
    return new Date(dateString).toLocaleDateString();
  };

  if (loading) {
    return (
      <Box sx={{ display: 'flex', justifyContent: 'center', p: 4 }}>
        <CircularProgress />
      </Box>
    );
  }

  return (
    <Box>
      <Box sx={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', mb: 3 }}>
        <Typography variant="h5" component="h2">
          Saved Polygons
        </Typography>
        <Button
          variant="outlined"
          startIcon={<RefreshIcon />}
          onClick={loadPolygons}
        >
          Refresh
        </Button>
      </Box>

      {error && (
        <Alert severity="error" onClose={() => setError('')} sx={{ mb: 2 }}>
          {error}
        </Alert>
      )}

      {polygons.length === 0 ? (
        <Card>
          <CardContent>
            <Typography variant="body1" color="text.secondary" align="center">
              No polygons saved yet. Draw a polygon to get started.
            </Typography>
          </CardContent>
        </Card>
      ) : (
        <Grid container spacing={3}>
          {polygons.map((polygon) => (
            <Grid item xs={12} md={6} lg={4} key={polygon.id}>
              <Card>
                <CardContent>
                  <Box sx={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start', mb: 2 }}>
                    <Typography variant="h6" component="h3">
                      {polygon.name}
                    </Typography>
                    <IconButton
                      size="small"
                      onClick={() => handleDelete(polygon.id)}
                      color="error"
                    >
                      <DeleteIcon />
                    </IconButton>
                  </Box>

                  <Box sx={{ mb: 2 }}>
                    <Chip 
                      label={formatArea(polygon.area_sq_meters)} 
                      color="success" 
                      size="small" 
                      sx={{ mr: 1, mb: 1 }}
                    />
                    <Chip 
                      label={formatPerimeter(polygon.perimeter_meters)} 
                      color="info" 
                      size="small" 
                      sx={{ mr: 1, mb: 1 }}
                    />
                  </Box>

                  <Typography variant="caption" color="text.secondary" display="block">
                    Created: {formatDate(polygon.created_at)}
                  </Typography>

                  <Box sx={{ mt: 2 }}>
                    <Button
                      variant="outlined"
                      size="small"
                      startIcon={<ViewIcon />}
                      onClick={() => handleViewOnMap(polygon)}
                      fullWidth
                    >
                      View on Map
                    </Button>
                  </Box>
                </CardContent>
              </Card>
            </Grid>
          ))}
        </Grid>
      )}

      <Dialog
        open={mapDialogOpen}
        onClose={() => setMapDialogOpen(false)}
        maxWidth="md"
        fullWidth
      >
        <DialogTitle>
          {selectedPolygon?.name} - Map View
        </DialogTitle>
        <DialogContent>
          <Box sx={{ height: '400px', width: '100%' }}>
            <GoogleMap
              center={{ lat: 40.7128, lng: -74.0060 }}
              zoom={10}
              onMapLoad={initializeMapWithPolygon}
            />
          </Box>
        </DialogContent>
        <DialogActions>
          <Button onClick={() => setMapDialogOpen(false)}>
            Close
          </Button>
        </DialogActions>
      </Dialog>
    </Box>
  );
};

export default PolygonList; 
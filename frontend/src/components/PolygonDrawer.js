import React, { useState, useEffect, useRef } from 'react';
import {
  Box,
  Paper,
  Typography,
  Button,
  TextField,
  Grid,
  Card,
  CardContent,
  Alert,
  CircularProgress,
  Divider
} from '@mui/material';
import {
  Save as SaveIcon,
  Clear as ClearIcon,
  Calculate as CalculateIcon
} from '@mui/icons-material';
import { polygonAPI } from '../services/api';
import GoogleMap from './GoogleMap';
import MetricsDisplay from './MetricsDisplay';

const PolygonDrawer = () => {
  const [map, setMap] = useState(null);
  const [drawingManager, setDrawingManager] = useState(null);
  const [polygon, setPolygon] = useState(null);
  const [polygonName, setPolygonName] = useState('');
  const [metrics, setMetrics] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');
  const [success, setSuccess] = useState('');

  const handleMapLoad = (mapInstance) => {
    if (!mapInstance) return;

    const drawingManagerInstance = new window.google.maps.drawing.DrawingManager({
      drawingMode: window.google.maps.drawing.OverlayType.POLYGON,
      drawingControl: true,
      drawingControlOptions: {
        position: window.google.maps.ControlPosition.TOP_CENTER,
        drawingModes: [window.google.maps.drawing.OverlayType.POLYGON],
      },
      polygonOptions: {
        fillColor: '#FF0000',
        fillOpacity: 0.3,
        strokeWeight: 2,
        strokeColor: '#FF0000',
        clickable: true,
        editable: true,
        zIndex: 1,
      },
    });

    drawingManagerInstance.setMap(mapInstance);

    window.google.maps.event.addListener(
      drawingManagerInstance,
      'polygoncomplete',
      (polygonInstance) => {
        setPolygon(polygonInstance);
        calculateMetrics(polygonInstance);
        
        window.google.maps.event.addListener(polygonInstance, 'set_at', () => {
          calculateMetrics(polygonInstance);
        });
        window.google.maps.event.addListener(polygonInstance, 'insert_at', () => {
          calculateMetrics(polygonInstance);
        });
      }
    );

    setMap(mapInstance);
    setDrawingManager(drawingManagerInstance);
  };

  const calculateMetrics = (polygonInstance) => {
    if (!polygonInstance) return;

    const path = polygonInstance.getPath();
    const coordinates = [];
    
    for (let i = 0; i < path.getLength(); i++) {
      const point = path.getAt(i);
      coordinates.push([point.lng(), point.lat()]);
    }

    const area = window.google.maps.geometry.spherical.computeArea(path);
    const perimeter = window.google.maps.geometry.spherical.computeLength(path);

    setMetrics({
      area: area,
      perimeter: perimeter,
      coordinates: coordinates,
    });
  };

  const clearPolygon = () => {
    if (polygon) {
      polygon.setMap(null);
      setPolygon(null);
    }
    setMetrics(null);
    setPolygonName('');
    setError('');
    setSuccess('');
  };

  const savePolygon = async () => {
    if (!metrics || !polygonName.trim()) {
      setError('Please provide a name for the polygon');
      return;
    }

    setLoading(true);
    setError('');
    setSuccess('');

    try {
      const polygonData = {
        name: polygonName.trim(),
        coordinates: metrics.coordinates,
      };

      const savedPolygon = await polygonAPI.create(polygonData);
      
      setSuccess(`Polygon "${savedPolygon.name}" saved successfully!`);
      setPolygonName('');
      
      setTimeout(() => {
        clearPolygon();
      }, 2000);
      
    } catch (err) {
      setError(err.response?.data?.message || 'Failed to save polygon');
    } finally {
      setLoading(false);
    }
  };

  return (
    <Box sx={{ height: '100%', display: 'flex', flexDirection: 'column' }}>
      <Grid container spacing={3} sx={{ height: '100%' }}>
        <Grid item xs={12} md={8} sx={{ height: '100%' }}>
          <Paper 
            elevation={3} 
            sx={{ 
              height: '100%', 
              minHeight: '500px',
              position: 'relative'
            }}
          >
            <GoogleMap
              center={{ lat: 40.7128, lng: -74.0060 }}
              zoom={10}
              onMapLoad={handleMapLoad}
            />
          </Paper>
        </Grid>

        <Grid item xs={12} md={4}>
          <Box sx={{ display: 'flex', flexDirection: 'column', gap: 2 }}>
            <Card>
              <CardContent>
                <Typography variant="h6" gutterBottom>
                  Draw Polygon
                </Typography>
                <Typography variant="body2" color="text.secondary">
                  Use the drawing tools above the map to create a polygon. 
                  Click on the map to add points, and double-click to complete the polygon.
                </Typography>
              </CardContent>
            </Card>

            <Card>
              <CardContent>
                <Typography variant="h6" gutterBottom>
                  Polygon Details
                </Typography>
                <TextField
                  fullWidth
                  label="Polygon Name"
                  value={polygonName}
                  onChange={(e) => setPolygonName(e.target.value)}
                  placeholder="Enter polygon name"
                  variant="outlined"
                  size="small"
                  sx={{ mb: 2 }}
                />
                
                <Box sx={{ display: 'flex', gap: 1 }}>
                  <Button
                    variant="contained"
                    startIcon={<SaveIcon />}
                    onClick={savePolygon}
                    disabled={!metrics || !polygonName.trim() || loading}
                    fullWidth
                  >
                    {loading ? <CircularProgress size={20} /> : 'Save Polygon'}
                  </Button>
                  
                  <Button
                    variant="outlined"
                    startIcon={<ClearIcon />}
                    onClick={clearPolygon}
                    disabled={!polygon}
                  >
                    Clear
                  </Button>
                </Box>
              </CardContent>
            </Card>

            {metrics && (
              <MetricsDisplay metrics={metrics} />
            )}

            {error && (
              <Alert severity="error" onClose={() => setError('')}>
                {error}
              </Alert>
            )}
            
            {success && (
              <Alert severity="success" onClose={() => setSuccess('')}>
                {success}
              </Alert>
            )}
          </Box>
        </Grid>
      </Grid>
    </Box>
  );
};

export default PolygonDrawer; 
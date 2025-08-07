import React from 'react';
import {
  Card,
  CardContent,
  Typography,
  Box,
  Divider,
  Chip
} from '@mui/material';
import {
  SquareFoot as AreaIcon,
  Straighten as PerimeterIcon,
  Calculate as CalculateIcon
} from '@mui/icons-material';

const MetricsDisplay = ({ metrics }) => {
  if (!metrics) return null;

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

  const formatCoordinates = (coordinates) => {
    return `${coordinates.length} points`;
  };

  return (
    <Card>
      <CardContent>
        <Box sx={{ display: 'flex', alignItems: 'center', mb: 2 }}>
          <CalculateIcon sx={{ mr: 1, color: 'primary.main' }} />
          <Typography variant="h6">
            Polygon Metrics
          </Typography>
        </Box>

        <Divider sx={{ mb: 2 }} />

        <Box sx={{ display: 'flex', flexDirection: 'column', gap: 2 }}>
          <Box sx={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between' }}>
            <Box sx={{ display: 'flex', alignItems: 'center' }}>
              <AreaIcon sx={{ mr: 1, color: 'success.main' }} />
              <Typography variant="body1">Area:</Typography>
            </Box>
            <Chip 
              label={formatArea(metrics.area)} 
              color="success" 
              variant="outlined"
            />
          </Box>

          <Box sx={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between' }}>
            <Box sx={{ display: 'flex', alignItems: 'center' }}>
              <PerimeterIcon sx={{ mr: 1, color: 'info.main' }} />
              <Typography variant="body1">Perimeter:</Typography>
            </Box>
            <Chip 
              label={formatPerimeter(metrics.perimeter)} 
              color="info" 
              variant="outlined"
            />
          </Box>

          <Box sx={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between' }}>
            <Typography variant="body1">Coordinates:</Typography>
            <Chip 
              label={formatCoordinates(metrics.coordinates)} 
              color="default" 
              variant="outlined"
            />
          </Box>
        </Box>

        <Box sx={{ mt: 2, pt: 2, borderTop: 1, borderColor: 'divider' }}>
          <Typography variant="caption" color="text.secondary">
            * Area and perimeter are calculated using spherical trigonometry
          </Typography>
        </Box>
      </CardContent>
    </Card>
  );
};

export default MetricsDisplay; 
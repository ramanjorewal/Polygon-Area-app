import React, { useEffect, useRef } from 'react';
import { Box } from '@mui/material';

const GoogleMap = ({ 
  center = { lat: 40.7128, lng: -74.0060 }, 
  zoom = 10,
  onMapLoad,
  children 
}) => {
  const mapRef = useRef(null);
  const mapInstanceRef = useRef(null);

  useEffect(() => {
    if (!window.google) {
      const script = document.createElement('script');
      script.src = `https://maps.googleapis.com/maps/api/js?key=AIzaSyDA0sUyUbr9wDC1CKNHYeFxSL7ZHZqgBhg&libraries=geometry,drawing`;
      script.async = true;
      script.defer = true;
      script.onload = initializeMap;
      document.head.appendChild(script);
    } else {
      initializeMap();
    }

    return () => {
      if (mapInstanceRef.current) {
      }
    };
  }, []);

  const initializeMap = () => {
    if (!mapRef.current || !window.google) return;

    try {
      const map = new window.google.maps.Map(mapRef.current, {
        center,
        zoom,
        mapTypeId: window.google.maps.MapTypeId.ROADMAP,
        mapTypeControl: true,
        streetViewControl: true,
        fullscreenControl: true,
      });

      mapInstanceRef.current = map;

      if (onMapLoad) {
        onMapLoad(map);
      }
    } catch (error) {
      console.error('Error creating map:', error);
    }
  };

  return (
    <Box
      ref={mapRef}
      sx={{
        width: '100%',
        height: '100%',
        minHeight: '400px',
      }}
    >
      {children}
    </Box>
  );
};

export default GoogleMap; 
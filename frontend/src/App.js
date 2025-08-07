import React, { useState } from 'react';
import {
  AppBar,
  Toolbar,
  Typography,
  Container,
  Box,
  Tabs,
  Tab,
  Paper,
  CssBaseline,
  ThemeProvider,
  createTheme
} from '@mui/material';
import {
  Map as MapIcon,
  List as ListIcon
} from '@mui/icons-material';
import PolygonDrawer from './components/PolygonDrawer';
import PolygonList from './components/PolygonList';

const theme = createTheme({
  palette: {
    primary: {
      main: '#1976d2',
    },
    secondary: {
      main: '#dc004e',
    },
  },
});

function App() {
  const [activeTab, setActiveTab] = useState(0);

  const handleTabChange = (event, newValue) => {
    setActiveTab(newValue);
  };

  return (
    <ThemeProvider theme={theme}>
      <CssBaseline />
      <Box sx={{ flexGrow: 1 }}>
        <AppBar position="static">
          <Toolbar>
            <Typography variant="h6" component="div" sx={{ flexGrow: 1 }}>
              Polygon Mapper
            </Typography>
          </Toolbar>
        </AppBar>
        
        <Container maxWidth="xl" sx={{ mt: 3, mb: 3 }}>
          <Paper sx={{ width: '100%' }}>
            <Tabs
              value={activeTab}
              onChange={handleTabChange}
              indicatorColor="primary"
              textColor="primary"
              centered
            >
              <Tab 
                icon={<MapIcon />} 
                label="Draw Polygon" 
                iconPosition="start"
              />
              <Tab 
                icon={<ListIcon />} 
                label="Saved Polygons" 
                iconPosition="start"
              />
            </Tabs>
          </Paper>
          
          <Box sx={{ mt: 3 }}>
            {activeTab === 0 && (
              <PolygonDrawer />
            )}
            {activeTab === 1 && (
              <PolygonList />
            )}
          </Box>
        </Container>
      </Box>
    </ThemeProvider>
  );
}

export default App; 
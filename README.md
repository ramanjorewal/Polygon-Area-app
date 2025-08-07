# Polygon Mapper

A full-stack web application for drawing, calculating, and managing geographical polygons with real-time area and perimeter calculations.

## Features

- **Interactive Map Drawing**: Draw polygons directly on Google Maps
- **Real-time Metrics**: Calculate area and perimeter as you draw
- **Data Persistence**: Save polygons to PostgreSQL database
- **Polygon Management**: View, delete, and visualize saved polygons
- **Responsive Design**: Works on desktop and mobile devices
- **Modern UI**: Clean Material-UI interface

## Tech Stack

### Backend
- **Django 4.2** with Django REST Framework
- **PostgreSQL** with spatial data support
- **Shapely** for geometry calculations
- **Python 3.8+**

### Frontend
- **React 18** with functional components and hooks
- **Material-UI (MUI)** for modern, responsive design
- **Google Maps JavaScript API** with Drawing Library
- **Axios** for API communication

## Quick Start

### Prerequisites
- Python 3.8+
- Node.js 16+
- PostgreSQL
- Google Maps API key

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd polygon-mapper
   ```

2. **Run the setup script**
   ```bash
   python setup.py
   ```

3. **Configure environment variables**
   - Edit `.env` file with your values
   - Set your Google Maps API key
   - Configure PostgreSQL connection

4. **Start the application**
   ```bash
   python start_app.py
   ```

5. **Access the application**
   - Frontend: http://localhost:3000
   - Backend API: http://localhost:8000/api/
   - Admin Panel: http://localhost:8000/admin/

## Environment Variables

### Backend (.env)
```bash
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

DB_NAME=polygon_db
DB_USER=postgres
DB_PASSWORD=your-password
DB_HOST=localhost
DB_PORT=5432

GOOGLE_MAPS_API_KEY=your-google-maps-api-key
```

### Frontend (.env)
```bash
REACT_APP_GOOGLE_MAPS_API_KEY=your-google-maps-api-key
REACT_APP_API_BASE_URL=http://localhost:8000/api
```

## API Endpoints

- `GET /api/polygons/` - List all polygons
- `POST /api/polygons/` - Create a new polygon
- `GET /api/polygons/{id}/` - Get specific polygon
- `DELETE /api/polygons/{id}/` - Delete polygon
- `GET /api/polygons/{id}/geojson/` - Get polygon as GeoJSON
- `GET /api/polygons/geojson_collection/` - Get all polygons as GeoJSON

## Usage

1. **Draw a Polygon**: Use the drawing tools on the map to create polygons
2. **View Metrics**: Real-time area and perimeter calculations
3. **Save Polygons**: Store polygons with names and metadata
4. **Manage Polygons**: View, delete, and visualize saved polygons

## Development

### Backend Commands
```bash
cd backend
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

### Frontend Commands
```bash
cd frontend
npm install
npm start
```

## License

MIT License

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request 
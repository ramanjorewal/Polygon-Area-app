#!/usr/bin/env python3

# Manually update the .env file with correct values
env_content = """# Django Settings
SECRET_KEY=0z5@+-)h-h!5v*99(46p@n-dblvjg=!3)8w94v2#kta3h+(x$a
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# Database
DB_NAME=polygondb
DB_USER=postgres
DB_PASSWORD=Ayaag@123
DB_HOST=localhost
DB_PORT=5432

# Google Maps API
GOOGLE_MAPS_API_KEY=your-google-maps-api-key-here

# Frontend Environment Variables
REACT_APP_GOOGLE_MAPS_API_KEY=your-google-maps-api-key-here
REACT_APP_API_BASE_URL=http://localhost:8000/api
"""

with open('.env', 'w') as f:
    f.write(env_content)

print("✅ .env file updated with correct values!")
print("✅ SECRET_KEY: 0z5@+-)h-h!5v*99(46p@n-dblvjg=!3)8w94v2#kta3h+(x$a")
print("✅ DB_PASSWORD: Ayaag@123")
print("✅ DB_NAME: polygondb") 
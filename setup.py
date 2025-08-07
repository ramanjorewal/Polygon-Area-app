#!/usr/bin/env python3
"""
Setup script for Polygon Mapper Application
"""

import os
import sys
import subprocess
import platform

def check_prerequisites():
    """Check if required tools are installed."""
    print("🔍 Checking prerequisites...")
    
    # Check Python
    try:
        result = subprocess.run(['python', '--version'], capture_output=True, text=True)
        if result.returncode == 0:
            print("✅ python --version")
        else:
            print("❌ Python not found")
            return False
    except FileNotFoundError:
        print("❌ Python not found")
        return False
    
    # Check Node.js
    try:
        result = subprocess.run(['node', '--version'], capture_output=True, text=True)
        if result.returncode == 0:
            print("✅ node --version")
        else:
            print("❌ Node.js not found")
            return False
    except FileNotFoundError:
        print("❌ Node.js not found")
        return False
    
    # Check npm
    try:
        result = subprocess.run(['npm', '--version'], capture_output=True, text=True)
        if result.returncode == 0:
            print("✅ npm --version")
        else:
            print("❌ npm not found")
            return False
    except FileNotFoundError:
        print("❌ npm not found")
        return False
    
    print("✅ All prerequisites are installed")
    return True

def create_env_file():
    """Create .env file if it doesn't exist."""
    print("📝 Creating .env file...")
    
    env_file = '.env'
    
    # Only create if it doesn't exist
    if not os.path.exists(env_file):
        env_content = """# Django Settings
SECRET_KEY=your-secret-key-here-change-in-production
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# Database
DB_NAME=polygon_db
DB_USER=postgres
DB_PASSWORD=your-password-here
DB_HOST=localhost
DB_PORT=5432

# Google Maps API
GOOGLE_MAPS_API_KEY=your-google-maps-api-key-here

# Frontend Environment Variables
REACT_APP_GOOGLE_MAPS_API_KEY=your-google-maps-api-key-here
REACT_APP_API_BASE_URL=http://localhost:8000/api
"""
        
        with open(env_file, 'w') as f:
            f.write(env_content)
        
        print("✅ Created .env file")
        print("⚠️  Please update the .env file with your actual values")
    else:
        print("✅ .env file already exists")

def setup_backend():
    """Setup Django backend."""
    print("🔧 Setting up Django backend...")
    
    # Create virtual environment
    try:
        result = subprocess.run(['python', '-m', 'venv', 'venv'], capture_output=True, text=True)
        if result.returncode == 0:
            print("✅ python -m venv venv")
        else:
            print("❌ Failed to create virtual environment")
            return False
    except Exception as e:
        print(f"❌ Error creating virtual environment: {e}")
        return False
    
    # Install Python dependencies
    try:
        if platform.system() == "Windows":
            cmd = ['venv\\Scripts\\activate', '&&', 'pip', 'install', '-r', 'backend/requirements.txt']
            result = subprocess.run(' '.join(cmd), shell=True, capture_output=True, text=True)
        else:
            cmd = ['source', 'venv/bin/activate', '&&', 'pip', 'install', '-r', 'backend/requirements.txt']
            result = subprocess.run(' '.join(cmd), shell=True, capture_output=True, text=True)
        
        if result.returncode == 0:
            print("✅ venv\\Scripts\\activate && pip install -r backend/requirements.txt")
        else:
            print("❌ Failed to install Python dependencies")
            print(f"Error: {result.stderr}")
            return False
    except Exception as e:
        print(f"❌ Error installing dependencies: {e}")
        return False
    
    # Run Django migrations
    try:
        if platform.system() == "Windows":
            cmd = ['venv\\Scripts\\activate', '&&', 'cd', 'backend', '&&', 'python', 'manage.py', 'makemigrations']
            result = subprocess.run(' '.join(cmd), shell=True, capture_output=True, text=True)
        else:
            cmd = ['source', 'venv/bin/activate', '&&', 'cd', 'backend', '&&', 'python', 'manage.py', 'makemigrations']
            result = subprocess.run(' '.join(cmd), shell=True, capture_output=True, text=True)
        
        if result.returncode == 0:
            print("✅ venv\\Scripts\\activate && cd backend && python manage.py makemigrations")
        else:
            print("❌ Failed to create migrations")
            print(f"Error: {result.stderr}")
            return False
    except Exception as e:
        print(f"❌ Error creating migrations: {e}")
        return False
    
    # Run Django migrate
    try:
        if platform.system() == "Windows":
            cmd = ['venv\\Scripts\\activate', '&&', 'cd', 'backend', '&&', 'python', 'manage.py', 'migrate']
            result = subprocess.run(' '.join(cmd), shell=True, capture_output=True, text=True)
        else:
            cmd = ['source', 'venv/bin/activate', '&&', 'cd', 'backend', '&&', 'python', 'manage.py', 'migrate']
            result = subprocess.run(' '.join(cmd), shell=True, capture_output=True, text=True)
        
        if result.returncode == 0:
            print("✅ venv\\Scripts\\activate && cd backend && python manage.py migrate")
        else:
            print("❌ Failed to run migrations")
            print(f"Error: {result.stderr}")
            return False
    except Exception as e:
        print(f"❌ Error running migrations: {e}")
        return False
    
    return True

def setup_frontend():
    """Setup React frontend."""
    print("🔧 Setting up React frontend...")
    
    try:
        result = subprocess.run(['npm', 'install'], cwd='frontend', capture_output=True, text=True)
        if result.returncode == 0:
            print("✅ npm install")
        else:
            print("❌ Failed to install Node.js dependencies")
            print(f"Error: {result.stderr}")
            return False
    except Exception as e:
        print(f"❌ Error installing Node.js dependencies: {e}")
        return False
    
    return True

def main():
    """Main setup function."""
    print("🚀 Setting up Polygon Mapper Application")
    print("=" * 50)
    print()
    
    # Check prerequisites
    if not check_prerequisites():
        print("❌ Prerequisites check failed")
        sys.exit(1)
    
    print()
    
    # Create .env file
    create_env_file()
    
    print()
    
    # Setup backend
    if not setup_backend():
        print("❌ Backend setup failed")
        sys.exit(1)
    
    print()
    
    # Setup frontend
    if not setup_frontend():
        print("❌ Frontend setup failed")
        sys.exit(1)
    
    print()
    print("🎉 Setup completed successfully!")
    print("=" * 50)
    print()
    print("📋 Next steps:")
    print("1. Update the .env file with your Google Maps API key")
    print("2. Run: python start.py")
    print("3. Open http://localhost:3000 in your browser")
    print()
    print("🔧 Development commands:")
    print("- Backend: cd backend && venv\\Scripts\\activate && python manage.py runserver")
    print("- Frontend: cd frontend && npm start")
    print()

if __name__ == "__main__":
    main() 
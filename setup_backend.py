#!/usr/bin/env python3
"""
Backend-only setup script for Polygon Mapper Application
"""

import os
import sys
import subprocess
import platform

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

def main():
    """Main setup function."""
    print("🚀 Setting up Polygon Mapper Backend")
    print("=" * 50)
    print()
    
    # Setup backend
    if not setup_backend():
        print("❌ Backend setup failed")
        sys.exit(1)
    
    print()
    print("🎉 Backend setup completed successfully!")
    print("=" * 50)
    print()
    print("📋 Next steps:")
    print("1. Start the backend: cd backend && venv\\Scripts\\activate && python manage.py runserver")
    print("2. The API will be available at http://localhost:8000/api/")
    print()
    print("🔧 Development commands:")
    print("- Backend: cd backend && venv\\Scripts\\activate && python manage.py runserver")
    print("- Create superuser: cd backend && venv\\Scripts\\activate && python manage.py createsuperuser")
    print()

if __name__ == "__main__":
    main() 
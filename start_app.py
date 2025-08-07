#!/usr/bin/env python3
"""
Startup script for Polygon Mapper Application
"""

import os
import sys
import subprocess
import platform
import time
import webbrowser
from pathlib import Path

def start_backend():
    """Start the Django backend server."""
    print("🚀 Starting Django backend...")
    
    try:
        # Use a more reliable approach for Windows
        if platform.system() == "Windows":
            # Create a batch command that activates venv and starts Django
            batch_content = """@echo off
call venv\\Scripts\\activate
cd backend
python manage.py runserver
"""
            with open('start_backend.bat', 'w') as f:
                f.write(batch_content)
            
            process = subprocess.Popen(['start_backend.bat'], shell=True)
        else:
            cmd = ['source', 'venv/bin/activate', '&&', 'cd', 'backend', '&&', 'python', 'manage.py', 'runserver']
            process = subprocess.Popen(' '.join(cmd), shell=True)
        
        print("✅ Backend server started at http://localhost:8000")
        return process
    except Exception as e:
        print(f"❌ Error starting backend: {e}")
        return None

def start_frontend():
    """Start the React frontend server."""
    print("🚀 Starting React frontend...")
    
    try:
        # Use a more reliable approach for Windows
        if platform.system() == "Windows":
            # Create a batch command that starts npm
            batch_content = """@echo off
cd frontend
npm start
"""
            with open('start_frontend.bat', 'w') as f:
                f.write(batch_content)
            
            process = subprocess.Popen(['start_frontend.bat'], shell=True)
        else:
            process = subprocess.Popen(['npm', 'start'], cwd='frontend')
        
        print("✅ Frontend server started at http://localhost:3000")
        return process
    except Exception as e:
        print(f"❌ Error starting frontend: {e}")
        return None

def main():
    """Main startup function."""
    print("🎯 Starting Polygon Mapper Application")
    print("=" * 50)
    print()
    
    # Check if .env file exists
    if not os.path.exists('.env'):
        print("❌ .env file not found! Please run setup first.")
        sys.exit(1)
    
    # Start backend
    backend_process = start_backend()
    if not backend_process:
        print("❌ Failed to start backend")
        sys.exit(1)
    
    # Wait a moment for backend to start
    print("⏳ Waiting for backend to initialize...")
    time.sleep(3)
    
    # Start frontend
    frontend_process = start_frontend()
    if not frontend_process:
        print("❌ Failed to start frontend")
        backend_process.terminate()
        sys.exit(1)
    
    print()
    print("🎉 Application started successfully!")
    print("=" * 50)
    print()
    print("📱 Frontend: http://localhost:3000")
    print("🔧 Backend API: http://localhost:8000/api/")
    print("👨‍💼 Admin Panel: http://localhost:8000/admin/")
    print()
    print("⚠️  Important Notes:")
    print("- Update your Google Maps API key in .env file for full functionality")
    print("- Press Ctrl+C to stop both servers")
    print()
    
    # Open browser after a short delay
    print("🌐 Opening application in browser...")
    time.sleep(5)
    webbrowser.open('http://localhost:3000')
    
    try:
        # Keep the script running
        print("🔄 Servers are running... Press Ctrl+C to stop")
        backend_process.wait()
        frontend_process.wait()
    except KeyboardInterrupt:
        print("\n🛑 Stopping servers...")
        backend_process.terminate()
        frontend_process.terminate()
        print("✅ Servers stopped")

if __name__ == "__main__":
    main() 
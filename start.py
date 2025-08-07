#!/usr/bin/env python3
"""
Quick start script for Polygon Mapper application.
"""
import os
import subprocess
import sys
import time
import webbrowser
from pathlib import Path


def run_command(command, cwd=None, background=False):
    """Run a command and return the process."""
    try:
        if background:
            process = subprocess.Popen(
                command,
                shell=True,
                cwd=cwd,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE
            )
            return process
        else:
            result = subprocess.run(
                command,
                shell=True,
                check=True,
                cwd=cwd,
                capture_output=True,
                text=True
            )
            print(f"✅ {command}")
            return True
    except subprocess.CalledProcessError as e:
        print(f"❌ {command}")
        print(f"Error: {e.stderr}")
        return False


def check_environment():
    """Check if environment is properly set up."""
    print("🔍 Checking environment...")
    
    # Check if .env file exists
    if not Path(".env").exists():
        print("❌ .env file not found. Please run setup.py first.")
        return False
    
    # Check if virtual environment exists
    venv_path = Path("venv")
    if not venv_path.exists():
        print("❌ Virtual environment not found. Please run setup.py first.")
        return False
    
    # Check if node_modules exists
    frontend_node_modules = Path("frontend/node_modules")
    if not frontend_node_modules.exists():
        print("❌ Frontend dependencies not installed. Please run setup.py first.")
        return False
    
    print("✅ Environment looks good!")
    return True


def start_backend():
    """Start Django backend server."""
    print("\n🚀 Starting Django backend...")
    
    # Activate virtual environment and start Django
    if os.name == 'nt':  # Windows
        activate_cmd = "venv\\Scripts\\activate"
    else:  # Unix/Linux/Mac
        activate_cmd = "source venv/bin/activate"
    
    django_cmd = f"{activate_cmd} && cd backend && python manage.py runserver"
    
    return run_command(django_cmd, background=True)


def start_frontend():
    """Start React frontend server."""
    print("\n🚀 Starting React frontend...")
    
    return run_command("npm start", cwd="frontend", background=True)


def main():
    """Main function to start the application."""
    print("🎯 Starting Polygon Mapper Application")
    print("=" * 50)
    
    # Check environment
    if not check_environment():
        print("\n💡 To set up the environment, run:")
        print("python setup.py")
        return False
    
    # Start backend
    backend_process = start_backend()
    if not backend_process:
        print("❌ Failed to start backend")
        return False
    
    # Wait a moment for backend to start
    print("⏳ Waiting for backend to start...")
    time.sleep(3)
    
    # Start frontend
    frontend_process = start_frontend()
    if not frontend_process:
        print("❌ Failed to start frontend")
        backend_process.terminate()
        return False
    
    print("\n🎉 Application started successfully!")
    print("\n📱 Access the application:")
    print("   Frontend: http://localhost:3000")
    print("   Backend API: http://localhost:8000/api/")
    print("   Django Admin: http://localhost:8000/admin/")
    
    # Open browser
    try:
        webbrowser.open("http://localhost:3000")
    except:
        pass
    
    print("\n⏹️  Press Ctrl+C to stop the application")
    
    try:
        # Keep the script running
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n🛑 Stopping application...")
        backend_process.terminate()
        frontend_process.terminate()
        print("✅ Application stopped")
    
    return True


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1) 
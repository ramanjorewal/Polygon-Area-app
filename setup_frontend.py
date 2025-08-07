#!/usr/bin/env python3
"""
Frontend setup script for Polygon Mapper Application
"""

import os
import sys
import subprocess
import platform

def setup_frontend():
    """Setup React frontend."""
    print("🔧 Setting up React frontend...")
    
    # Check if frontend directory exists
    if not os.path.exists('frontend'):
        print("❌ Frontend directory not found!")
        return False
    
    # Install Node.js dependencies
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
    print("🚀 Setting up Polygon Mapper Frontend")
    print("=" * 50)
    print()
    
    # Setup frontend
    if not setup_frontend():
        print("❌ Frontend setup failed")
        sys.exit(1)
    
    print()
    print("🎉 Frontend setup completed successfully!")
    print("=" * 50)
    print()
    print("📋 Next steps:")
    print("1. Start the frontend: cd frontend && npm start")
    print("2. The app will be available at http://localhost:3000")
    print()
    print("🔧 Development commands:")
    print("- Frontend: cd frontend && npm start")
    print("- Build: cd frontend && npm run build")
    print()
    print("⚠️  Note: Make sure to update your Google Maps API key in the .env file")
    print("   before starting the frontend for full functionality.")

if __name__ == "__main__":
    main() 
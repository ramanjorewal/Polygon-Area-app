#!/usr/bin/env python3
"""
Status script for Polygon Mapper Application
"""

import os
import sys

def check_setup_status():
    """Check the current setup status."""
    print("📊 Polygon Mapper Application Status")
    print("=" * 50)
    print()
    
    # Check .env file
    if os.path.exists('.env'):
        print("✅ .env file exists")
    else:
        print("❌ .env file missing")
        return False
    
    # Check virtual environment
    if os.path.exists('venv'):
        print("✅ Virtual environment exists")
    else:
        print("❌ Virtual environment missing")
        return False
    
    # Check backend
    if os.path.exists('backend'):
        print("✅ Backend directory exists")
    else:
        print("❌ Backend directory missing")
        return False
    
    # Check frontend
    if os.path.exists('frontend'):
        print("✅ Frontend directory exists")
        if os.path.exists('frontend/node_modules'):
            print("✅ Frontend dependencies installed")
        else:
            print("⚠️  Frontend dependencies not installed")
    else:
        print("❌ Frontend directory missing")
        return False
    
    return True

def show_next_steps():
    """Show next steps for the user."""
    print()
    print("🎯 Next Steps:")
    print("=" * 30)
    print()
    print("1. 🔑 Update Google Maps API Key:")
    print("   - Edit .env file")
    print("   - Replace 'your-google-maps-api-key-here' with your actual API key")
    print()
    print("2. 🚀 Start the Application:")
    print("   - Run: python start_app.py")
    print("   - This will start both backend and frontend servers")
    print()
    print("3. 🌐 Access the Application:")
    print("   - Frontend: http://localhost:3000")
    print("   - Backend API: http://localhost:8000/api/")
    print("   - Admin Panel: http://localhost:8000/admin/")
    print()
    print("4. 👨‍💼 Create Admin User (Optional):")
    print("   - cd backend")
    print("   - venv\\Scripts\\activate")
    print("   - python manage.py createsuperuser")
    print()
    print("🔧 Manual Commands:")
    print("- Backend: cd backend && venv\\Scripts\\activate && python manage.py runserver")
    print("- Frontend: cd frontend && npm start")
    print()

def main():
    """Main status function."""
    if check_setup_status():
        print()
        print("🎉 Setup appears to be complete!")
        show_next_steps()
    else:
        print()
        print("❌ Setup is incomplete. Please run the setup scripts first.")
        print()
        print("📋 Setup Commands:")
        print("- Backend: python setup_backend.py")
        print("- Frontend: python setup_frontend.py")

if __name__ == "__main__":
    main() 
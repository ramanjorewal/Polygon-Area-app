#!/usr/bin/env python3
"""
Script to update the .env file with correct database password.
"""

import os
import re

def update_env_file():
    """Update the .env file with correct values."""
    
    env_file = '.env'
    
    if not os.path.exists(env_file):
        print("❌ .env file not found!")
        return False
    
    # Read the current .env file
    with open(env_file, 'r') as f:
        content = f.read()
    
    # Update SECRET_KEY
    secret_key = "0z5@+-)h-h!5v*99(46p@n-dblvjg=!3)8w94v2#kta3h+(x$a"
    content = re.sub(
        r'SECRET_KEY=.*',
        f'SECRET_KEY={secret_key}',
        content
    )
    
    # Get the actual password from user
    print("🔐 Database Password Update")
    print("=" * 40)
    print("Please enter your PostgreSQL password:")
    password = input("Password: ").strip()
    
    if not password:
        print("❌ Password cannot be empty!")
        return False
    
    # Update DB_PASSWORD
    content = re.sub(
        r'DB_PASSWORD=.*',
        f'DB_PASSWORD={password}',
        content
    )
    
    # Write the updated content back
    with open(env_file, 'w') as f:
        f.write(content)
    
    print("✅ .env file updated successfully!")
    print(f"✅ SECRET_KEY: {secret_key}")
    print(f"✅ DB_PASSWORD: {password}")
    
    return True

if __name__ == "__main__":
    try:
        if update_env_file():
            print("\n🚀 Now you can run: python setup.py")
        else:
            print("\n❌ Failed to update .env file")
    except Exception as e:
        print(f"❌ Error: {e}") 
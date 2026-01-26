#!/usr/bin/env python
"""
Password Reset Script for Django
This script allows you to reset a user's password.

Usage:
    python reset_password.py <username> <new_password>
    
Or run interactively:
    python reset_password.py
"""

import os
import sys
import django

# Setup Django
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password

User = get_user_model()


def reset_password(username, new_password):
    """
    Reset password for a user.
    
    Algorithm used: PBKDF2 with SHA256
    - Format: pbkdf2_sha256$600000$salt$hash
    - Iterations: 600,000
    - Hash function: SHA256
    """
    try:
        user = User.objects.get(username=username)
        user.set_password(new_password)
        user.save()
        print(f"✅ Password successfully reset for user: {username}")
        print(f"📝 New password hash algorithm: PBKDF2-SHA256")
        print(f"🔐 Password stored in format: pbkdf2_sha256$600000$<salt>$<hash>")
        return True
    except User.DoesNotExist:
        print(f"❌ User '{username}' not found!")
        return False
    except Exception as e:
        print(f"❌ Error: {e}")
        return False


def interactive_reset():
    """Interactive password reset."""
    print("\n" + "="*50)
    print("🔐 Django Password Reset Tool")
    print("="*50)
    print("\nAlgorithm: PBKDF2 with SHA256")
    print("Iterations: 600,000")
    print("Format: pbkdf2_sha256$600000$salt$hash")
    print("\n" + "-"*50 + "\n")
    
    username = input("Enter username: ").strip()
    if not username:
        print("❌ Username cannot be empty!")
        return
    
    try:
        user = User.objects.get(username=username)
        print(f"✅ Found user: {user.username} (Email: {user.email or 'N/A'})")
    except User.DoesNotExist:
        print(f"❌ User '{username}' not found!")
        return
    
    new_password = input("Enter new password: ").strip()
    if not new_password:
        print("❌ Password cannot be empty!")
        return
    
    confirm = input("Confirm new password: ").strip()
    if new_password != confirm:
        print("❌ Passwords do not match!")
        return
    
    # Reset password
    user.set_password(new_password)
    user.save()
    
    print(f"\n✅ Password successfully reset for user: {username}")
    print(f"📝 Password hash algorithm: PBKDF2-SHA256")
    print(f"🔐 Stored format: pbkdf2_sha256$600000$<salt>$<hash>")


if __name__ == "__main__":
    if len(sys.argv) == 3:
        # Command line mode
        username = sys.argv[1]
        new_password = sys.argv[2]
        reset_password(username, new_password)
    elif len(sys.argv) == 1:
        # Interactive mode
        interactive_reset()
    else:
        print("Usage:")
        print("  python reset_password.py <username> <new_password>")
        print("  python reset_password.py  (interactive mode)")
        sys.exit(1)

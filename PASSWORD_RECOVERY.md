# 🔐 Admin Password Recovery Guide

If you forget your Django admin password, here are **3 easy methods** to reset it:

---

## Method 1: Using Django Management Command (Recommended) ⭐

**Easiest and most Django-native way:**

```bash
cd /Users/gobinddas1999gmail.com/Documents/BangaVidyarthiNewsPortal
source venv/bin/activate
python manage.py reset_admin_password <username> <new_password>
```

**Example:**
```bash
python manage.py reset_admin_password admin MyNewPassword123
```

**Output:**
```
✅ Successfully reset password for user: admin
📝 You can now login with the new password.
```

---

## Method 2: Using Python Script

**Using the standalone reset script:**

### Interactive Mode (Recommended):
```bash
source venv/bin/activate
python reset_password.py
```

The script will:
1. Ask for username
2. Show user details
3. Ask for new password
4. Confirm password
5. Reset the password

### Command Line Mode:
```bash
python reset_password.py <username> <new_password>
```

**Example:**
```bash
python reset_password.py admin MyNewPassword123
```

---

## Method 3: Using Django Shell

**For advanced users who want full control:**

```bash
source venv/bin/activate
python manage.py shell
```

Then in the Python shell:
```python
from django.contrib.auth import get_user_model
User = get_user_model()

# Get your admin user
user = User.objects.get(username='admin')  # Replace 'admin' with your username

# Reset password
user.set_password('YourNewPassword123')
user.save()

print("Password reset successfully!")
exit()
```

---

## Method 4: Create a New Superuser (If you don't know username)

**If you forgot both username and password:**

```bash
source venv/bin/activate
python manage.py createsuperuser
```

This will create a new admin account. You can then:
- Use the new account
- Or use it to reset the old account's password

---

## Quick Reference

### Find Your Admin Username:
```bash
python manage.py shell
```

Then:
```python
from django.contrib.auth import get_user_model
User = get_user_model()
superusers = User.objects.filter(is_superuser=True)
for user in superusers:
    print(f"Username: {user.username}, Email: {user.email}")
exit()
```

---

## Security Notes

⚠️ **Important:**
- Passwords are **hashed** (one-way encryption) - they cannot be "recovered"
- You can only **reset** them to a new password
- The password hashing algorithm used: **PBKDF2 with SHA256**
- Format: `pbkdf2_sha256$600000$<salt>$<hash>`

---

## Troubleshooting

### "User not found" error:
- Check the username is correct (case-sensitive)
- List all users using Django shell (see above)

### "Permission denied" error:
- Make sure you're in the project directory
- Activate virtual environment: `source venv/bin/activate`

### Script not working:
- Ensure Django is properly installed
- Check you're using the correct Python environment
- Verify `DJANGO_SETTINGS_MODULE` is set correctly

---

## After Resetting

1. Go to admin panel: `http://localhost:8000/admin`
2. Login with your username and **new password**
3. Consider changing it to something memorable (but secure!)

---

**Need help?** Check the script files:
- `reset_password.py` - Standalone Python script
- `news/management/commands/reset_admin_password.py` - Django command

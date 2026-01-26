# 👤 Change Admin Username Guide

If you want to change your Django admin username, here are **3 easy methods**:

---

## Method 1: Using Django Management Command (Recommended) ⭐

**Easiest and most Django-native way:**

```bash
cd /Users/gobinddas1999gmail.com/Documents/BangaVidyarthiNewsPortal
source venv/bin/activate
python manage.py change_admin_username <old_username> <new_username>
```

**Example:**
```bash
python manage.py change_admin_username admin newadmin
```

**Output:**
```
✅ Successfully changed username!
   Old username: admin
   New username: newadmin
📝 You can now login with the new username.
```

---

## Method 2: Using Django Admin Panel

**If you can still login with current username:**

1. Go to admin panel: `http://localhost:8000/admin`
2. Login with your current username
3. Click on **"Users"** in the admin panel
4. Find and click on your user account
5. Change the **"Username"** field
6. Click **"Save"**

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
user = User.objects.get(username='old_username')  # Replace with your current username

# Check if new username exists
new_username = 'new_username'  # Your desired new username
if User.objects.filter(username=new_username).exists():
    print(f"❌ Username '{new_username}' already exists!")
else:
    # Change username
    old_username = user.username
    user.username = new_username
    user.save()
    print(f"✅ Username changed from '{old_username}' to '{new_username}'")
    exit()
```

---

## Quick Reference

### List All Admin Users:
```bash
python manage.py shell
```

Then:
```python
from django.contrib.auth import get_user_model
User = get_user_model()
superusers = User.objects.filter(is_superuser=True)
for user in superusers:
    print(f"Username: {user.username}, Email: {user.email}, Is Superuser: {user.is_superuser}")
exit()
```

### Check if Username Exists:
```bash
python manage.py shell
```

Then:
```python
from django.contrib.auth import get_user_model
User = get_user_model()
username = 'desired_username'
if User.objects.filter(username=username).exists():
    print(f"❌ Username '{username}' already exists!")
else:
    print(f"✅ Username '{username}' is available!")
exit()
```

---

## Important Notes

⚠️ **Things to remember:**

1. **Username must be unique** - Django doesn't allow duplicate usernames
2. **Case-sensitive** - `Admin` and `admin` are different usernames
3. **No spaces** - Usernames cannot contain spaces
4. **After changing** - You'll need to login with the **new username**
5. **Email can be same** - Multiple users can have the same email (but not recommended)

---

## Troubleshooting

### "Username already exists" error:
- The new username is already taken
- Choose a different username
- Check existing usernames using Django shell (see above)

### "User not found" error:
- Check the old username is correct (case-sensitive)
- List all users using Django shell (see above)

### "Permission denied" error:
- Make sure you're in the project directory
- Activate virtual environment: `source venv/bin/activate`

---

## Change Both Username and Password

If you want to change both username and password:

```bash
# Step 1: Change username
python manage.py change_admin_username old_username new_username

# Step 2: Change password
python manage.py reset_admin_password new_username new_password
```

---

## After Changing Username

1. Go to admin panel: `http://localhost:8000/admin`
2. Login with your **new username** and password
3. Verify everything works correctly

---

**Need help?** Check the command file:
- `news/management/commands/change_admin_username.py` - Django command

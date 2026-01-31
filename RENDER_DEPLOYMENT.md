# Render Deployment Guide

## Quick Setup on Render

### 1. Create Web Service on Render
1. Go to [render.com](https://render.com)
2. Click **"New +"** → **"Web Service"**
3. Connect your GitHub repo: `Gobind-Das/news-web`
4. Select branch: `main`

### 2. Configure Web Service
- **Name:** `news-portal` (or your choice)
- **Environment:** `Python 3`
- **Build Command:** 
  ```
  pip install -r requirements.txt && python manage.py collectstatic --noinput
  ```
- **Start Command:** 
  ```
  gunicorn config.wsgi
  ```

### 3. Add Environment Variables
Go to **"Environment"** tab and add these variables:

| Key | Value |
|-----|-------|
| `SECRET_KEY` | Generate one: `python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"` |
| `DEBUG` | `False` |
| `ALLOWED_HOSTS` | `your-app-name.onrender.com` |
| `DATABASE_URL` | (Auto-populated if you add PostgreSQL below) |

### 4. Add PostgreSQL Database (Optional but Recommended)
1. In the same Render dashboard, click **"New +"** → **"PostgreSQL"**
2. Create a new PostgreSQL database
3. Render will auto-populate `DATABASE_URL` in your Web Service

### 5. Deploy
Click **"Deploy"** and watch the logs. Render will:
- Install dependencies
- Run `collectstatic` 
- Start your app with gunicorn

Visit `https://your-app-name.onrender.com` once deployment completes.

## Verify Deployment
Check logs in Render dashboard for any errors. Common issues:
- Missing `SECRET_KEY` or `DEBUG` env var
- `ALLOWED_HOSTS` doesn't match your Render domain
- Database connection failed (if using PostgreSQL)

## Local Testing Before Deploy
To test locally with production settings:
```bash
DEBUG=False SECRET_KEY=test-key python manage.py runserver
```

## Updates & Redeployment
- Push changes to `main` branch
- Render auto-redeploys (if "Auto Deploy" is enabled)
- Or manually click "Manual Deploy" in Render dashboard

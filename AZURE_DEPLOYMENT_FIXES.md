# Azure & Render Deployment Fixes

This document outlines the fixes made to resolve deployment issues with both Azure App Service and Render.

---

## Multi-Platform Database Configuration

The application is configured to work on **Render** (PostgreSQL via DATABASE_URL), **Azure App Service** (PostgreSQL via individual DB_* variables), and **local development** (SQLite).

### How It Works

```python
# Multi-platform database configuration:
# - Priority 1: Render - Uses DATABASE_URL environment variable (PostgreSQL)
# - Priority 2: Azure - Uses individual DB_* environment variables (PostgreSQL)
# - Priority 3: Local - Falls back to SQLite for development
if os.environ.get('DATABASE_URL'):
    # Render configuration - use dj_database_url for PostgreSQL
    DATABASES = {
        "default": dj_database_url.config(
            default=os.environ.get('DATABASE_URL'),
            conn_max_age=600,
            ssl_require=not DEBUG,
        )
    }
elif os.environ.get('DB_ENGINE'):
    # Azure configuration - use individual DB_* environment variables for PostgreSQL
    DATABASES = {
        'default': {
            'ENGINE': os.environ.get('DB_ENGINE'),
            'NAME': os.environ.get('DB_NAME'),
            'USER': os.environ.get('DB_USER'),
            'PASSWORD': os.environ.get('DB_PASSWORD'),
            'HOST': os.environ.get('DB_HOST'),
            'PORT': os.environ.get('DB_PORT', '5432'),
            'OPTIONS': {
                'sslmode': 'require',
            },
        }
    }
else:
    # Local development fallback to SQLite
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
```

### Platform Configuration

| Platform | Configuration Method | Database Used |
|----------|---------------------|---------------|
| Render   | `DATABASE_URL` env var | PostgreSQL via dj_database_url |
| Azure    | Individual `DB_*` env vars | PostgreSQL via psycopg2 |
| Local Dev | None | SQLite (local file) |

---

## Azure App Service Configuration

### Required Environment Variables for Azure PostgreSQL

Add these environment variables in **Azure Portal → App Service → Configuration → Application settings**:

| Variable | Value | Example |
|----------|-------|---------|
| `DB_ENGINE` | `django.db.backends.postgresql` | `django.db.backends.postgresql` |
| `DB_NAME` | Your database name | `lensmaster_db` |
| `DB_USER` | Database username | `lensmaster_admin` |
| `DB_PASSWORD` | Database password | `your-secure-password` |
| `DB_HOST` | PostgreSQL server hostname | `lensmaster-server.postgres.database.azure.com` |
| `DB_PORT` | PostgreSQL port (default: 5432) | `5432` |
| `SECRET_KEY` | Django secret key | `your-django-secret-key` |
| `DEBUG` | Set to False in production | `False` |
| `ALLOWED_HOSTS` | Your Azure domain | `lensmasterpro-xxx.azurewebsites.net` |

### Optional Environment Variables

| Variable | Purpose | Example |
|----------|---------|---------|
| `CLOUDINARY_CLOUD_NAME` | Cloudinary cloud name | `your-cloud-name` |
| `CLOUDINARY_API_KEY` | Cloudinary API key | `123456789012345` |
| `CLOUDINARY_API_SECRET` | Cloudinary API secret | `your-api-secret` |

### Azure PostgreSQL Setup

1. **Create Azure Database for PostgreSQL** (Flexible Server recommended)
2. **Configure networking** to allow Azure services access
3. **Add environment variables** to App Service Configuration
4. **Run migrations** via SSH or deployment script:
   ```bash
   python manage.py migrate
   python manage.py collectstatic --noinput
   ```

---

## Issues Fixed

### 1. Database Configuration Error (Fixed)

**Problem:** App crashing with `django.core.exceptions.ImproperlyConfigured: settings.DATABASES is improperly configured. Please supply the ENGINE value.`

**Root Cause:** `dj_database_url.config()` returns an incomplete dict when `DATABASE_URL` is not set.

**Solution:** Check if `DATABASE_URL` exists before using `dj_database_url.config()`, otherwise fall back to SQLite.

---

### 2. DisallowedHost Error (Fixed - Latest)

**Problem:** `ERROR:django.security.DisallowedHost:Invalid HTTP_HOST header: '169.254.130.4:8000'`

**Root Cause:** Azure's internal health check uses IP `169.254.130.4` as the Host header.

**Solution:** Added Azure internal health check IPs to ALLOWED_HOSTS:

```python
ALLOWED_HOSTS.extend([
    # ... existing hosts ...
    '169.254.130.4',  # Azure health check IP
    '169.254.130.1',  # Additional Azure internal IP  
    '0.0.0.0',        # Catch-all for internal traffic
])
```

---

## Files Changed

1. `lensmaster_pro/settings.py` - Fixed database configuration and ALLOWED_HOSTS
2. `AZURE_DEPLOYMENT_FIXES.md` - This documentation file

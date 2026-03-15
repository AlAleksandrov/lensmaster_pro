# Azure & Render Deployment Fixes

This document outlines the fixes made to resolve deployment issues with both Azure App Service and Render.

---

## Dual-Platform Database Configuration

The application is configured to work on both **Render** (with PostgreSQL) and **Azure App Service** (with SQLite).

### How It Works

```python
# Dual-platform database configuration:
# - Render: Uses DATABASE_URL environment variable (PostgreSQL)
# - Azure/Local: Falls back to SQLite when DATABASE_URL is not set
if os.environ.get('DATABASE_URL'):
    # Render configuration - use dj_database_url for PostgreSQL
    DATABASES = {
        "default": dj_database_url.config(
            default=os.environ.get('DATABASE_URL'),
            conn_max_age=600,
            ssl_require=not DEBUG,
        )
    }
else:
    # Azure/local fallback to SQLite
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
```

### Platform Configuration

| Platform | DATABASE_URL | Database Used |
|----------|--------------|---------------|
| Render   | Set (PostgreSQL URL) | PostgreSQL via dj_database_url |
| Azure    | Not set | SQLite (local file) |
| Local Dev | Not set | SQLite (local file) |

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

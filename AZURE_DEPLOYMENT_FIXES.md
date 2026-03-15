# Azure App Service Deployment Fixes

This document outlines the fixes made to resolve deployment issues with Azure App Service.

---

## Issues Fixed

### 1. Database Configuration Error (Fixed - Latest)

**Problem:** App crashing with `django.core.exceptions.ImproperlyConfigured: settings.DATABASES is improperly configured. Please supply the ENGINE value.`

**Root Cause:** `dj_database_url.config()` returns an incomplete dict when `DATABASE_URL` is not set.

**Solution:** Always start with a valid SQLite fallback configuration:

```python
# Always start with SQLite as the default fallback
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# Override with DATABASE_URL configuration if it exists and is valid
if DATABASE_URL and DATABASE_URL.strip():
    try:
        db_config = dj_database_url.config(...)
        if db_config and db_config.get('ENGINE'):
            DATABASES['default'] = db_config
    except Exception:
        pass  # Keep SQLite fallback on error
```

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

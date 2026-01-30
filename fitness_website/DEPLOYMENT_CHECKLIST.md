# Deployment Checklist - FitLife Fitness Website

## Pre-Deployment Checklist

### 1. Security Settings

#### Django Settings (settings.py)
- [ ] Set `DEBUG = False`
- [ ] Update `SECRET_KEY` (use environment variable)
- [ ] Configure `ALLOWED_HOSTS` with your domain
- [ ] Set up `SECURE_SSL_REDIRECT = True`
- [ ] Enable `SECURE_HSTS_SECONDS`
- [ ] Set `SESSION_COOKIE_SECURE = True`
- [ ] Set `CSRF_COOKIE_SECURE = True`
- [ ] Configure `SECURE_BROWSER_XSS_FILTER = True`
- [ ] Set `X_FRAME_OPTIONS = 'DENY'`

```python
# Production settings example
DEBUG = False
SECRET_KEY = os.environ.get('SECRET_KEY')
ALLOWED_HOSTS = ['yourdomain.com', 'www.yourdomain.com']

SECURE_SSL_REDIRECT = True
SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_BROWSER_XSS_FILTER = True
X_FRAME_OPTIONS = 'DENY'
```

#### Password & Authentication
- [ ] Change default admin password
- [ ] Remove or disable test accounts
- [ ] Review user permissions
- [ ] Set strong password requirements
- [ ] Enable two-factor authentication (optional)

### 2. Database Configuration

#### PostgreSQL Setup (Recommended)
- [ ] Install PostgreSQL
- [ ] Create production database
- [ ] Create database user with limited permissions
- [ ] Update database settings in Django

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DB_NAME'),
        'USER': os.environ.get('DB_USER'),
        'PASSWORD': os.environ.get('DB_PASSWORD'),
        'HOST': os.environ.get('DB_HOST'),
        'PORT': os.environ.get('DB_PORT', '5432'),
    }
}
```

#### Database Migration
- [ ] Run `python manage.py makemigrations`
- [ ] Run `python manage.py migrate`
- [ ] Create database backup strategy
- [ ] Set up automated backups

### 3. Static Files & Media

#### Static Files
- [ ] Run `python manage.py collectstatic`
- [ ] Configure static file serving (Nginx/Apache)
- [ ] Set up CDN (optional but recommended)
- [ ] Configure `STATIC_ROOT` and `STATIC_URL`

```python
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'
```

#### Media Files
- [ ] Configure `MEDIA_ROOT` and `MEDIA_URL`
- [ ] Set up media file storage (S3, Azure, etc.)
- [ ] Configure file upload limits
- [ ] Set up image optimization

```python
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
```

### 4. Environment Variables

#### Required Variables
- [ ] `SECRET_KEY` - Django secret key
- [ ] `DEBUG` - Set to False
- [ ] `DATABASE_URL` - Database connection string
- [ ] `ALLOWED_HOSTS` - Comma-separated list of domains

#### Optional Variables
- [ ] `EMAIL_HOST` - SMTP server
- [ ] `EMAIL_PORT` - SMTP port
- [ ] `EMAIL_HOST_USER` - Email username
- [ ] `EMAIL_HOST_PASSWORD` - Email password
- [ ] `AWS_ACCESS_KEY_ID` - For S3 storage
- [ ] `AWS_SECRET_ACCESS_KEY` - For S3 storage

#### .env File Example
```
SECRET_KEY=your-secret-key-here
DEBUG=False
DATABASE_URL=postgresql://user:password@localhost/dbname
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password
```

### 5. Web Server Configuration

#### Nginx Configuration
- [ ] Install Nginx
- [ ] Configure server blocks
- [ ] Set up SSL certificates (Let's Encrypt)
- [ ] Configure proxy pass to Gunicorn
- [ ] Set up static file serving
- [ ] Configure gzip compression

#### Gunicorn Setup
- [ ] Install Gunicorn: `pip install gunicorn`
- [ ] Create Gunicorn configuration
- [ ] Set up systemd service
- [ ] Configure workers and threads

```bash
# Gunicorn command
gunicorn fitness_website.wsgi:application --bind 0.0.0.0:8000 --workers 3
```

### 6. Performance Optimization

#### Caching
- [ ] Install Redis: `pip install redis django-redis`
- [ ] Configure Django cache backend
- [ ] Implement view caching
- [ ] Set up template fragment caching

```python
CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://127.0.0.1:6379/1',
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        }
    }
}
```

#### Database Optimization
- [ ] Add database indexes
- [ ] Optimize queries (use select_related, prefetch_related)
- [ ] Enable query logging
- [ ] Set up connection pooling

#### CDN Setup
- [ ] Configure CloudFlare or similar CDN
- [ ] Set up static file caching
- [ ] Configure image optimization
- [ ] Enable HTTP/2

### 7. Monitoring & Logging

#### Error Tracking
- [ ] Set up Sentry or similar service
- [ ] Configure error notifications
- [ ] Set up logging levels
- [ ] Configure log rotation

```python
# Sentry configuration
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

sentry_sdk.init(
    dsn="your-sentry-dsn",
    integrations=[DjangoIntegration()],
    traces_sample_rate=1.0,
)
```

#### Logging Configuration
- [ ] Configure Django logging
- [ ] Set up application logs
- [ ] Configure access logs
- [ ] Set up error logs

```python
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'filename': '/var/log/django/error.log',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'ERROR',
            'propagate': True,
        },
    },
}
```

#### Monitoring Tools
- [ ] Set up uptime monitoring (UptimeRobot, Pingdom)
- [ ] Configure performance monitoring (New Relic, DataDog)
- [ ] Set up server monitoring (CPU, RAM, Disk)
- [ ] Configure database monitoring

### 8. Backup Strategy

#### Database Backups
- [ ] Set up automated daily backups
- [ ] Configure backup retention policy
- [ ] Test backup restoration
- [ ] Store backups off-site

```bash
# PostgreSQL backup script
pg_dump -U username dbname > backup_$(date +%Y%m%d).sql
```

#### Media File Backups
- [ ] Set up media file backups
- [ ] Configure incremental backups
- [ ] Test file restoration
- [ ] Use cloud storage (S3, Azure)

#### Code Backups
- [ ] Use Git for version control
- [ ] Push to remote repository (GitHub, GitLab)
- [ ] Tag releases
- [ ] Document deployment process

### 9. Email Configuration

#### SMTP Setup
- [ ] Configure email backend
- [ ] Set up SMTP credentials
- [ ] Test email sending
- [ ] Configure email templates

```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
DEFAULT_FROM_EMAIL = 'noreply@yourdomain.com'
```

#### Email Features
- [ ] Welcome emails for new users
- [ ] Password reset emails
- [ ] Notification emails
- [ ] Admin alert emails

### 10. Testing

#### Pre-Deployment Testing
- [ ] Run all unit tests: `python manage.py test`
- [ ] Test user registration and login
- [ ] Test admin panel functionality
- [ ] Test all CRUD operations
- [ ] Test calculators
- [ ] Test form validations
- [ ] Test on multiple browsers
- [ ] Test on mobile devices
- [ ] Load testing (optional)

#### Security Testing
- [ ] Run security checks: `python manage.py check --deploy`
- [ ] Test HTTPS redirect
- [ ] Test CSRF protection
- [ ] Test SQL injection prevention
- [ ] Test XSS protection
- [ ] Scan for vulnerabilities

### 11. Documentation

#### User Documentation
- [ ] Update README.md
- [ ] Create user guide
- [ ] Document API endpoints (if any)
- [ ] Create FAQ section

#### Admin Documentation
- [ ] Update ADMIN_PANEL_GUIDE.md
- [ ] Document deployment process
- [ ] Create troubleshooting guide
- [ ] Document backup procedures

#### Technical Documentation
- [ ] Document server configuration
- [ ] Document database schema
- [ ] Create architecture diagram
- [ ] Document third-party integrations

### 12. Domain & SSL

#### Domain Setup
- [ ] Purchase domain name
- [ ] Configure DNS records
- [ ] Set up A records
- [ ] Configure CNAME records
- [ ] Set up MX records (for email)

#### SSL Certificate
- [ ] Install Certbot
- [ ] Generate SSL certificate
- [ ] Configure auto-renewal
- [ ] Test HTTPS access
- [ ] Force HTTPS redirect

```bash
# Let's Encrypt SSL
sudo certbot --nginx -d yourdomain.com -d www.yourdomain.com
```

### 13. Deployment Process

#### Initial Deployment
1. [ ] Clone repository to server
2. [ ] Create virtual environment
3. [ ] Install dependencies: `pip install -r requirements.txt`
4. [ ] Set up environment variables
5. [ ] Run migrations
6. [ ] Collect static files
7. [ ] Create superuser
8. [ ] Start Gunicorn
9. [ ] Configure Nginx
10. [ ] Test deployment

#### Deployment Script Example
```bash
#!/bin/bash
cd /var/www/fitness_website
git pull origin main
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py collectstatic --noinput
sudo systemctl restart gunicorn
sudo systemctl restart nginx
```

### 14. Post-Deployment

#### Verification
- [ ] Test website accessibility
- [ ] Verify SSL certificate
- [ ] Test all major features
- [ ] Check error logs
- [ ] Monitor server resources
- [ ] Test email functionality

#### Monitoring Setup
- [ ] Set up uptime alerts
- [ ] Configure error notifications
- [ ] Monitor server performance
- [ ] Track user analytics (Google Analytics)

#### Maintenance Plan
- [ ] Schedule regular updates
- [ ] Plan backup verification
- [ ] Schedule security audits
- [ ] Plan performance reviews

### 15. Compliance & Legal

#### Privacy & Data Protection
- [ ] Create privacy policy
- [ ] Create terms of service
- [ ] Implement GDPR compliance (if applicable)
- [ ] Add cookie consent banner
- [ ] Document data retention policy

#### Accessibility
- [ ] Test with screen readers
- [ ] Verify keyboard navigation
- [ ] Check color contrast
- [ ] Add alt text to images
- [ ] Test with accessibility tools

## Quick Deployment Commands

### Development to Production Migration
```bash
# 1. Export data from development
python manage.py dumpdata > data.json

# 2. On production server
python manage.py loaddata data.json

# 3. Create superuser
python manage.py createsuperuser

# 4. Collect static files
python manage.py collectstatic --noinput

# 5. Run migrations
python manage.py migrate
```

### Server Management
```bash
# Start Gunicorn
gunicorn fitness_website.wsgi:application --bind 0.0.0.0:8000

# Restart services
sudo systemctl restart gunicorn
sudo systemctl restart nginx

# Check logs
sudo journalctl -u gunicorn
sudo tail -f /var/log/nginx/error.log
```

## Deployment Platforms

### Heroku
- [ ] Install Heroku CLI
- [ ] Create Heroku app
- [ ] Add PostgreSQL addon
- [ ] Configure environment variables
- [ ] Deploy: `git push heroku main`

### AWS (EC2)
- [ ] Launch EC2 instance
- [ ] Configure security groups
- [ ] Install dependencies
- [ ] Set up RDS for database
- [ ] Configure S3 for media files

### DigitalOcean
- [ ] Create droplet
- [ ] Configure firewall
- [ ] Install required software
- [ ] Set up managed database
- [ ] Configure Spaces for media

### Docker Deployment
- [ ] Create Dockerfile
- [ ] Create docker-compose.yml
- [ ] Build image: `docker build -t fitness-website .`
- [ ] Run container: `docker-compose up -d`

## Rollback Plan

### If Deployment Fails
1. [ ] Keep previous version accessible
2. [ ] Document rollback procedure
3. [ ] Test rollback process
4. [ ] Have database backup ready
5. [ ] Communicate with users

### Rollback Steps
```bash
# 1. Switch to previous version
git checkout previous-tag

# 2. Restore database backup
psql dbname < backup.sql

# 3. Restart services
sudo systemctl restart gunicorn nginx
```

## Support & Maintenance

### Regular Maintenance Tasks
- [ ] Weekly: Check error logs
- [ ] Weekly: Review server resources
- [ ] Monthly: Update dependencies
- [ ] Monthly: Security patches
- [ ] Quarterly: Performance review
- [ ] Yearly: Security audit

### Emergency Contacts
- [ ] Server provider support
- [ ] Database administrator
- [ ] DNS provider support
- [ ] SSL certificate provider

---

## Final Checklist

Before going live:
- [ ] All items above are checked
- [ ] Backup strategy is in place
- [ ] Monitoring is configured
- [ ] Documentation is complete
- [ ] Team is trained
- [ ] Support plan is ready

**Status:** Ready for deployment! 🚀

---

**Remember:** Always test in a staging environment before deploying to production!
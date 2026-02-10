# HTTPS Deployment Configuration

## SSL/TLS Setup
The application is designed to run behind a web server such as Nginx or Apache
configured with SSL/TLS certificates.

Example tools:
- Let's Encrypt (Certbot)
- Cloud provider SSL termination

## Django HTTPS Enforcement
Django enforces HTTPS using:
- SECURE_SSL_REDIRECT
- HTTP Strict Transport Security (HSTS)
- Secure cookies for session and CSRF protection

All HTTP requests are automatically redirected to HTTPS.


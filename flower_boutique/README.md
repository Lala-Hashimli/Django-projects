# Flower Boutique

Flower Boutique is a web application built with **Django** for managing and displaying a variety of flower products. It allows users to browse flowers, filter by category, and view product details. Admins can manage flowers, categories, and monitor product status.

---

## Features

- Browse flowers by category, color, and rating
- View product details, including images and pricing
- Admin panel with full CRUD functionality for flowers and categories
- Automatic handling of product expiration dates
- Rating system with visual stars
- Easy management of product status: Pending, Approved, Rejected, Expired

---

## Technology Stack

- **Backend:** Django
- **Database:** SQLite (or PostgreSQL/MySQL if configured)
- **Asynchronous Tasks:** Celery with Redis
- **Frontend:** HTML, CSS (Bootstrap optional)
- **Python Version:** 3.13

---
# Create and activate a virtual environment:
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

# Install dependencies:
pip install -r requirements.txt

# Apply migrations:
python manage.py migrate

# Create a superuser:
python manage.py createsuperuser

# Run the development server:
python manage.py runserver

# Celery Setup
# 1.Start Redis server (or another broker).
# 2.Start Celery worker:
celery -A proj worker --pool=solo --loglevel=INFO

# Optional: Run Celery beat for scheduled tasks:
celery -A proj beat --loglevel=INFO


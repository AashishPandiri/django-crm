# Django CRM with MySQL
A simple and effective Customer Relationship Management (CRM) system built with Django and MySQL, designed to help small businesses manage customer records and interactions efficiently.

- Customer Record Management: Add, view, edit, and delete customer records
- User Authentication: Secure login and registration system
- User-friendly Interface: Clean and responsive web interface
- MySQL Database: Reliable data storage with MySQL
- Admin Panel: Django admin interface for advanced management

## Project Structure

```
django-crm/
├── dcrm/                       # Main Django project configuration
│   ├── asgi.py                 # ASGI configuration for async support
│   ├── settings.py             # Django settings and configuration
│   ├── urls.py                 # Main URL routing
│   ├── wsgi.py                 # WSGI configuration for deployment
│   └── __init__.py             # Python package initialization
├── manage.py                   # Django management script
├── mydb.py                     # Database setup/configuration script
└── website/                    # Main CRM application
    ├── admin.py                # Django admin configuration
    ├── apps.py                 # App configuration
    ├── forms.py                # Django forms for user input
    ├── migrations/             # Database migrations
    │   ├── 0001_initial.py
    │   └── __init__.py
    ├── models.py               # Database models
    ├── templates/              # HTML templates
    │   ├── add_record.html         # Add new customer record
    │   ├── base.html               # Base template layout
    │   ├── home.html               # Homepage/dashboard
    │   ├── navbar.html             # Navigation bar component
    │   ├── record.html             # View individual record
    │   ├── register.html           # User registration
    │   └── update_record.html     # Update existing record
    ├── tests.py               # Unit tests
    ├── urls.py                # App-specific URL routing
    ├── views.py               # View functions/classes
    └── __init__.py            # Python package initialization
```

## Technology Stack
```
Backend: Django
Database: MySQL+
Frontend: HTML, Bootstrap
Authentication: Django built-in authentication system
Database Connector: mysqlclient
```

## Installation
1. Clone the Repository
```
git clone https://github.com/AashishPandiri/django-crm.git
cd django-crm
```
2. Create Virtual Environment
```
python -m venv crm_env
```
3. Activate Virtual Environment
```
On Windows:
crm_env\Scripts\activate
On macOS/Linux:
source crm_env/bin/activate
```
4. Install Dependencies
```
pip install django
pip install mysqlclient
If you encounter issues with mysqlclient, try:
pip install PyMySQL
```
5. MySQL Database Setup
```
python mydb.py
```
6. Configure Database Connection
```
Update the DATABASES setting in dcrm/settings.py:
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'dccrm',
        'USER': 'root',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```
7. Database Migration
```
python manage.py makemigrations
python manage.py migrate
```
8. Create Superuser
```
python manage.py createsuperuser
```
9. Run the Development Server
```
python manage.py runserver
```

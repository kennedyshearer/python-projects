# Django Job Application Form

A simple and clean Django web application for collecting job applications with email confirmation functionality.

## 🚀 Features

- **Job Application Form**: Collect applicant information including name, email, availability date, and current occupation
- **Email Confirmation**: Automatic email confirmation sent to applicants upon form submission
- **Responsive Design**: Built with Bootstrap 5 for mobile-friendly interface
- **Form Validation**: Client-side and server-side validation for all form fields
- **Admin Interface**: Django admin panel for managing submitted applications
- **SQLite Database**: Lightweight database for storing application data

## 📋 Form Fields

The application form collects the following information:
- First Name
- Last Name
- Email Address
- Available Start Date
- Current Occupation (Employed, Unemployed, Self-Employed, Student)

## 🛠️ Technology Stack

- **Backend**: Django 5.2.5
- **Database**: SQLite3
- **Frontend**: Bootstrap 5, HTML5, CSS3
- **Email**: Django SMTP backend with Gmail integration
- **Python**: 3.13+

## 📦 Installation

### Prerequisites

- Python 3.13 or higher
- pip (Python package installer)

### Setup Instructions

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd app16-django-form
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**
   
   **Windows:**
   ```bash
   venv\Scripts\activate
   ```
   
   **macOS/Linux:**
   ```bash
   source venv/bin/activate
   ```

4. **Install dependencies**
   ```bash
   pip install django
   ```

5. **Configure email settings**
   
   Edit `mysite/settings.py` and update the email configuration:
   ```python
   EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
   EMAIL_HOST = 'smtp.gmail.com'
   EMAIL_PORT = 587
   EMAIL_USE_TLS = True
   EMAIL_HOST_USER = 'your-email@gmail.com'
   EMAIL_HOST_PASSWORD = 'your-app-password'
   ```
   
   **Note**: For Gmail, you'll need to generate an App Password in your Google Account settings.
   
   **Alternative Email Providers:**
   
   **Outlook/Hotmail:**
   ```python
   EMAIL_HOST = 'smtp-mail.outlook.com'
   EMAIL_PORT = 587
   EMAIL_USE_TLS = True
   ```
   
   **Yahoo:**
   ```python
   EMAIL_HOST = 'smtp.mail.yahoo.com'
   EMAIL_PORT = 587
   EMAIL_USE_TLS = True
   ```
   
   **Custom SMTP Server:**
   ```python
   EMAIL_HOST = 'your-smtp-server.com'
   EMAIL_PORT = 587  # or 465 for SSL
   EMAIL_USE_TLS = True  # or False if using SSL
   EMAIL_USE_SSL = False  # Set to True if using port 465
   ```

6. **Run database migrations**
   ```bash
   python manage.py migrate
   ```

7. **Create a superuser (optional)**
   ```bash
   python manage.py createsuperuser
   ```

8. **Start the development server**
   ```bash
   python manage.py runserver
   ```

9. **Access the application**
   
   Open your browser and navigate to:
   - Main application: `http://127.0.0.1:8000/`
   - Admin panel: `http://127.0.0.1:8000/admin/`
   - About page: `http://127.0.0.1:8000/about/`

## 📁 Project Structure

```
app16-django-form/
├── job_application/          # Main Django app
│   ├── migrations/          # Database migrations
│   ├── templates/           # HTML templates
│   │   ├── base.html       # Base template with Bootstrap
│   │   ├── index.html      # Job application form
│   │   └── about.html      # About page
│   ├── admin.py            # Admin configuration
│   ├── forms.py            # Django form definitions
│   ├── models.py           # Database models
│   ├── urls.py             # URL routing
│   └── views.py            # View functions
├── mysite/                 # Django project settings
│   ├── settings.py         # Project configuration
│   ├── urls.py             # Main URL configuration
│   └── wsgi.py             # WSGI configuration
├── db.sqlite3              # SQLite database
├── manage.py               # Django management script
└── README.md               # This file
```

## 🎯 Usage

1. **Submit an Application**
   - Navigate to the home page
   - Fill out the job application form
   - Click "Submit" to send your application
   - You'll receive an email confirmation

2. **Admin Management**
   - Access the admin panel at `/admin/`
   - View and manage all submitted applications
   - Export data if needed

## ⚙️ Configuration

### Email Settings

The application is configured to use Gmail SMTP. To set up email functionality:

1. Enable 2-factor authentication on your Gmail account
2. Generate an App Password:
   - Go to Google Account settings
   - Security → 2-Step Verification → App passwords
   - Generate a password for "Mail"
3. Update the settings in `mysite/settings.py`

### Database

The application uses SQLite by default. For production, consider switching to PostgreSQL or MySQL by updating the `DATABASES` setting in `mysite/settings.py`.

## 🔧 Development

### Running Tests
```bash
python manage.py test
```

### Creating Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### Collecting Static Files (for production)
```bash
python manage.py collectstatic
```

## 🚀 Deployment

For production deployment:

1. Set `DEBUG = False` in `mysite/settings.py`
2. Configure `ALLOWED_HOSTS` with your domain
3. Set up a production database (PostgreSQL recommended)
4. Configure static file serving
5. Set up a web server (Nginx + Gunicorn recommended)
6. Use environment variables for sensitive settings

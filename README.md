# 🏥 MediTrack Pro

MediTrack Pro is a comprehensive medical tracking system designed to help healthcare professionals manage patient records, SOAP notes, and daily memos efficiently.

## ✨ Features

- 👤 Patient Management
- 📝 SOAP Notes Documentation
- 📅 Daily Memos
- 👥 User Role Management (Doctors & Nurses)
- 🔒 Secure Authentication System

## 🛠️ Tech Stack

- Django (Backend Framework)
- SQLite (Database)
- CKEditor (Rich Text Editing)

## 📁 Project Structure

```
meditrack/
├── core/                   # Core application module
│   ├── models.py          # Database models
│   ├── signals.py         # Django signals
│   └── apps.py           # App configuration
├── meditrack/             # Project configuration
│   ├── settings.py       # Project settings
│   ├── urls.py           # URL configurations
│   ├── asgi.py           # ASGI configuration
│   └── wsgi.py           # WSGI configuration
└── manage.py             # Django management script
```

## 💡 Models Documentation

### Patient Model
- Stores patient information including name, bangsal (ward), and room
- Fields: name, bangsal, room, created_at, updated_at

### SOAPNote Model
- Manages SOAP (Subjective, Objective, Assessment, Plan) notes for patients
- Fields:
  - patient (ForeignKey to Patient)
  - date
  - subjective, objective, assessment, plan (text fields)
  - image (optional medical image)
  - created_by (ForeignKey to User)
  - created_at, updated_at

### DailyMemo Model
- Handles daily memos/notes for medical staff
- Fields:
  - date
  - content (RichTextField for formatted text)
  - created_by (ForeignKey to User)
  - created_at, updated_at

### UserProfile Model
- Extends Django's User model with role-based access
- Fields:
  - user (OneToOneField to User)
  - role (doctor/nurse)

## 🚀 Getting Started

1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run migrations:
   ```bash
   python manage.py migrate
   ```
4. Create a superuser:
   ```bash
   python manage.py createsuperuser
   ```
5. Run the development server:
   ```bash
   python manage.py runserver
   ```

## 👩‍💻 Development Guide

### Adding New Features
1. Create models in `core/models.py`
2. Register models in `admin.py`
3. Create views and forms
4. Add URL patterns
5. Run migrations

### User Roles
- Doctors: Full access to all features
- Nurses: Limited access based on permissions

## 📝 License

This project is licensed under the MIT License.
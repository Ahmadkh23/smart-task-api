# Smart Task Manager

A modern, user-friendly task management application built with Django and Django REST Framework. Organize, prioritize, and track your daily tasks with an intuitive interface.

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Django](https://img.shields.io/badge/Django-5.2%2B-darkgreen)
![REST API](https://img.shields.io/badge/API-REST-orange)
![License](https://img.shields.io/badge/License-MIT-green)

## Features

✨ **Modern UI** - Clean, responsive design with an intuitive dashboard  
🔐 **Secure Authentication** - User registration and login with password validation  
📝 **Task Management** - Create, read, update, and delete tasks with ease  
🎯 **Priority Levels** - Organize tasks by low, medium, and high priority  
✅ **Task Completion** - Mark tasks as complete with visual feedback  
🔍 **Smart Filtering** - Filter tasks by status and priority  
📊 **Task Statistics** - View total and completed task counts  
💻 **Responsive Design** - Works seamlessly on desktop and mobile devices  
🔌 **REST API** - Full API for programmatic access to tasks  

## Tech Stack

- **Backend**: Django 5.2, Django REST Framework
- **Database**: SQLite (development)
- **Frontend**: HTML5, CSS3, Vanilla JavaScript
- **Authentication**: Django's built-in auth system

## Prerequisites

- Python 3.10 or higher
- pip (Python package manager)
- virtualenv (recommended)

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/smart-task-api.git
cd smart-task-api
```

### 2. Create and activate virtual environment

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run migrations

```bash
python manage.py migrate
```

### 5. Create a superuser (optional)

For admin panel access:

```bash
python manage.py createsuperuser
```

### 6. Start the development server

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` in your browser.

## Usage

### User Registration & Login

1. Visit the homepage
2. Click **Sign Up** to create a new account
3. Enter your username and password
4. Click **Sign In** to log in

### Managing Tasks

- **Add Task**: Enter task title, select priority, and click "Add Task"
- **Mark Complete**: Check the checkbox next to a task to mark it as complete
- **Delete Task**: Click "Delete" to remove a task
- **Filter Tasks**: Use filter buttons to view all, pending, completed, or high-priority tasks
- **View Statistics**: See total and completed task counts in the dashboard header

## API Endpoints

The application includes a REST API for programmatic access:

### Authentication

- `POST /login/` - User login
- `POST /register/` - User registration  
- `POST /logout/` - User logout

### Tasks (Requires Authentication)

- `GET /api/tasks/` - List all user's tasks
- `POST /api/tasks/` - Create a new task
- `GET /api/tasks/{id}/` - Get task details
- `PATCH /api/tasks/{id}/` - Update task
- `DELETE /api/tasks/{id}/` - Delete task

### Query Parameters

- `completed=true/false` - Filter by completion status
- `priority=low/medium/high` - Filter by priority
- `search=keyword` - Search in title and description
- `ordering=created_at,-due_date` - Sort results

### Example API Usage

```bash
# Login
curl -X POST http://localhost:8000/login/ \
  -d "username=myuser&password=mypass"

# List tasks (requires authentication)
curl -X GET http://localhost:8000/api/tasks/ \
  -H "Cookie: sessionid=YOUR_SESSION_ID"

# Create a task
curl -X POST http://localhost:8000/api/tasks/ \
  -H "Content-Type: application/json" \
  -H "Cookie: sessionid=YOUR_SESSION_ID" \
  -d '{"title": "Buy groceries", "priority": "high", "completed": false}'
```

## Project Structure

```
smart-task-api/
├── config/                 # Django project settings
│   ├── settings.py        # Project configuration
│   ├── urls.py            # URL routing
│   └── wsgi.py            # WSGI configuration
├── tasks/                 # Main application
│   ├── models.py          # Database models
│   ├── views.py           # View logic
│   ├── serializers.py     # DRF serializers
│   ├── urls.py            # App URL routing
│   └── migrations/        # Database migrations
├── templates/             # HTML templates
│   ├── base.html          # Base template with navbar
│   ├── auth/              # Authentication templates
│   │   ├── login.html     # Login page
│   │   └── register.html  # Registration page
│   └── tasks/             # Task templates
│       └── dashboard.html # Main dashboard
├── manage.py              # Django CLI
├── requirements.txt       # Python dependencies
└── README.md              # This file
```

## Database Models

### User (Django's built-in)

Handles user authentication and profile information.

### Task

| Field | Type | Description |
|-------|------|-------------|
| title | CharField | Task title (max 255 characters) |
| description | TextField | Detailed task description (optional) |
| completed | BooleanField | Task completion status |
| priority | CharField | Priority level (low, medium, high) |
| due_date | DateTimeField | Task deadline (optional) |
| created_at | DateTimeField | Task creation timestamp |
| owner | ForeignKey | Associated user |

## Configuration

### Environment Variables

Create a `.env` file in the project root (optional):

```env
DEBUG=True
SECRET_KEY=your-secret-key-here
ALLOWED_HOSTS=localhost,127.0.0.1
```

### Settings

Edit `config/settings.py` to configure:

- Database settings
- Allowed hosts
- Static files location
- Email configuration

## Running Tests

```bash
python manage.py test
```

## Development

### Create a new migration

```bash
python manage.py makemigrations
python manage.py migrate
```

### Access Django Admin Panel

```
http://127.0.0.1:8000/admin/
```

Use credentials from `createsuperuser` command.

## Deployment

### Using Gunicorn

```bash
pip install gunicorn
gunicorn config.wsgi:application --bind 0.0.0.0:8000
```

### Using Docker

Build and run with Docker:

```bash
docker build -t smart-task-api .
docker run -p 8000:8000 smart-task-api
```

### Production Checklist

- [ ] Set `DEBUG=False` in settings
- [ ] Update `ALLOWED_HOSTS` with your domain
- [ ] Use a secure `SECRET_KEY`
- [ ] Configure a production database (PostgreSQL recommended)
- [ ] Set up static files serving (Whitenoise, CloudFront, etc.)
- [ ] Enable HTTPS/SSL
- [ ] Configure email backend for notifications
- [ ] Set up logging and monitoring
- [ ] Run security check: `python manage.py check --deploy`

## Troubleshooting

### "ModuleNotFoundError: No module named 'django'"

Ensure virtual environment is activated and dependencies are installed:

```bash
source venv/bin/activate
pip install -r requirements.txt
```

### Database errors

Reset your database (development only):

```bash
rm db.sqlite3
python manage.py migrate
```

### Port already in use

Run on a different port:

```bash
python manage.py runserver 8080
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For issues, questions, or suggestions, please open an issue on GitHub or contact the maintainers.

## Acknowledgments

- Django documentation and community
- Django REST Framework
- Bootstrap for CSS inspiration
- All contributors and users

---

**Made with ❤️ for task management enthusiasts**

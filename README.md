# Smart Task API & Dashboard

A lightweight, full-stack task management application built with Django and Django REST Framework (DRF). This project features a robust RESTful API backend coupled with an elegant, responsive dark-mode web interface using vanilla JavaScript for real-time async data rendering.

## Features

- **Dynamic Frontend Dashboard:** A modern, single-page dark-mode web interface built using vanilla HTML/CSS and JavaScript.
- **Asynchronous CRUD Operations:** Create, Read, Update (Toggle Complete), and Delete tasks seamlessly without reloading the page using the Fetch API.
- **Task Prioritization:** Color-coded task cards based on priority metrics (`High`, `Medium`, `Low`).
- **Secure REST API Backend:** Built using Django REST Framework with built-in `BasicAuthentication` and `SessionAuthentication` classes.
- **CSRF Protection:** Integrated secure token handling for state-changing HTTP requests (`POST`, `PATCH`, `DELETE`).

##  Tech Stack

- **Backend Framework:** Django 5.x
- **API Engine:** Django REST Framework (DRF)
- **Frontend Architecture:** Vanilla JavaScript, HTML5, CSS3 (Modern Flexbox + Variables)
- **Language:** Python 3.x
- **Database:** SQLite (Relational)

##  Local Setup & Initialization

Follow this exact sequence inside your terminal to install dependencies, configure your local database, and spin up the development environment.

<Sequence>
  <Step title="Install Project Requirements" subtitle="Terminal Execution">
    Install the core framework, API toolkit, filtration utilities, and environment configurations:
    
```bash
    pip install django djangorestframework django-filter python-dotenv
    ```
  </Step>
  <Step title="Generate Migration Blueprints" subtitle="Django ORM Layer">
    Scan your applications for new structural model layouts or adjustments:
    
```bash
    python3 manage.py makemigrations
    ```
  </Step>
  <Step title="Apply Schema Migrations" subtitle="Database Layer">
    Execute your migration files to securely map out your relational SQLite database tables:
    
```bash
    python3 manage.py migrate
    ```
  </Step>
  <Step title="Launch Development Server" subtitle="Local Environment">
    Boot up your local backend engine and interface dashboard layout:
    
```bash
    python3 manage.py runserver
    ```
  </Step>
</Sequence>

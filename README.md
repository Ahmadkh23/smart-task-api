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

##  Local Setup & Installation

Follow these steps to spin up the project locally on your machine:

1. **Clone the repository:**
   
```bash
   git clone [https://github.com/Ahmadkh123/smart-task-api.git](https://github.com/Ahmadkh123/smart-task-api.git)
   cd smart-task-api

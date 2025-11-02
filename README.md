# My Django Portfolio Site

This is a minimal, two-page Django project to demonstrate the MVT (Model-View-Template) flow.

## How to Run

1.  Clone this repository.
2.  Install Django (if not already installed):
    ```bash
    pip install django
    ```
3.  Navigate to the project's root directory (where `manage.py` is).
4.  Apply migrations (good practice, though not strictly needed for this app):
    ```bash
    python manage.py migrate
    ```
5.  Start the local development server:
    ```bash
    python manage.py runserver
    ```
6.  Open your web browser and go to: `http://127.0.0.1:8000/`
7.  To see the education page, go to: `http://127.0.0.1:8000/education/`
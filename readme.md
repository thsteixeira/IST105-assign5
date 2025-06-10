# IST105 Assignment 5 - Puzzle App

This is a Django-based web application for IST105 Assignment 5 by Thiago Teixeira. The app features a simple puzzle game where users can submit a number and a text message, and another user can try to guess the number.

## Features

- Submit a number and a text message.
- Guess the submitted number.
- User-friendly interface styled with CSS.

## Requirements

- Python 3.8+
- Django 4.x

## Setup Instructions

1. **Clone the repository** (if applicable) or download the project files.

2. **Create a virtual environment** (recommended):
    ```sh
    python -m venv venv
    ```

3. **Activate the virtual environment**:
    - On Windows:
        ```sh
        venv\Scripts\activate
        ```
    - On macOS/Linux:
        ```sh
        source venv/bin/activate
        ```

4. **Install dependencies**:
    ```sh
    pip install django
    ```

5. **Run migrations**:
    ```sh
    python manage.py migrate
    ```

6. **Run the development server**:
    ```sh
    python manage.py runserver
    ```

7. **Open your browser** and go to `http://127.0.0.1:8000/` to use the app.

## Project Structure

- `puzzleapp/forms.py` - Django forms for user input.
- `puzzleapp/templates/` - HTML templates for the app.
- `manage.py` - Django management script.

## Author

Thiago Teixeira

---

&copy; IST105 Assignment 5 - Thiago Teixeira. All rights reserved.
# Flask Todo List Application

## Problem Definition
The goal is to build a simple to-do list application using Flask and Python 12. The application should allow users to:
- Add new to-do items
- Mark items as completed
- Delete items from the list
- View all to-do items in a clean, simple interface

### Features
- User authentication (Login/Logout)
- Basic CRUD operations on to-do items (Create, Read, Update, Delete)
- Persist data in an SQLite database

### Constraints
- Code should be clean, well-structured, and follow best practices
- The application should be lightweight and easy to deploy
- The application should run on Python 12

### Technology Stack
- Backend: Python 12
- Web Framework: Flask
- Database: SQLite
- Environment: Virtual Environment (venv)

### Setup Instructions
- Install Python 12
- Set up a virtual environment
- Install dependencies using pip
- Run the application in the virtual environment

### Expected Outcomes
- A working to-do list web application with a REST API
- Proper error handling and validation
- Tests for the API endpoints

### Directory Structure
- `app.py`: The main Flask application file containing the routes and logic.
- `venv/`: The virtual environment directory (auto-generated).
- `requirements.txt`: File containing the list of dependencies for easy installation.
- `templates/`: Folder for HTML templates for the application's frontend (if applicable).
- `static/`: Folder for static files such as CSS, JavaScript, and images.
- `models/`: Folder for defining database models and other business logic.
- `tests/`: Folder for unit tests and API tests.
- `config/`: Folder for storing configuration files (e.g., database URI, secret keys). 
- `docs/internal/`: folder for internal documentation 
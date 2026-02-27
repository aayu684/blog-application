# Django Blog Application

A fully functional Blog Application built using Django and Bootstrap 5. It features user authentication, a complete CRUD (Create, Read, Update, Delete) system for blog posts, image uploading capabilities, search functionality, and pagination.

## Features

*   **User Authentication**: Secure Sign-up, Login, and Logout functionality.
*   **Post Management (CRUD)**:
    *   **Create**: Authenticated users can write new blog posts and optionally upload an image.
    *   **Read**: Anyone can view the list of blog posts and read individual posts.
    *   **Update**: Authors can edit their own posts.
    *   **Delete**: Authors can delete their own posts.
*   **Search**: Filter posts by keywords in the title or content.
*   **Pagination**: Navigational controls to limit the number of posts displayed per page.
*   **Responsive UI**: Styled beautifully with Bootstrap 5 components.
*   **Admin Dashboard**: Manage users and posts via Django's built-in Admin interface.

## Prerequisites

Before you begin, ensure you have the following installed:
*   [Python 3.8+](https://www.python.org/downloads/)
*   [Pip](https://pip.pypa.io/en/stable/installation/)
*   Git

## Installation & Setup

Follow these steps to get the project running on your local machine.

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/reponame.git
cd "reponame"
```

### 2. Create a Virtual Environment
It's highly recommended to use a virtual environment to manage dependencies.
**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```
**macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```
*(If `requirements.txt` is missing, manually install: `pip install django pillow`)*

### 4. Apply Database Migrations
Set up the SQLite database by running the standard Django migration commands:
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create a Superuser (Optional)
To access the Django Admin panel (`/admin`), create an administrative user:
```bash
python manage.py createsuperuser
```
Follow the prompts to set your username, email, and password.

### 6. Run the Development Server
```bash
python manage.py runserver
```

Open your web browser and navigate to `http://127.0.0.1:8000/` to view the application!

## Usage Guide
1. **Explore**: Browse the homepage to see the latest posts. Use the search bar for specific topics.
2. **Interact**: Click "Sign Up" to create a standard account.
3. **Publish**: Once logged in, click "New Post" in the navigation bar to start writing.
4. **Manage Admin**: Go to `http://127.0.0.1:8000/admin/` and log in with your superuser credentials to manage users, groups, and all blog entries globally.

## Built With
*   [Django 6.0](https://www.djangoproject.com/) - High-level Python Web framework.
*   [Bootstrap 5](https://getbootstrap.com/) - Front-end standard for responsive, mobile-first design.
*   [Pillow](https://python-pillow.org/) - Python Imaging Library (PIL) fork for handling image uploads.
*   **SQLite** - Default lightweight database utilized by Django out-of-the-box.

---
*BY - Aayushi Soni.*

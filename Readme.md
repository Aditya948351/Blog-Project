# Django Course - Module: Blog Project

Welcome to the **Blog Project** module of the Django Course! In this section, we will take everything we've learned about Django basics—models, views, templates, and URLs—and apply it to build a real-world blogging platform.

## 🎯 Learning Objectives

By the end of this module, you will be able to:
- Structure a Django project with multiple applications (`blogapp`, `authorapp`, `categoryapp`).
- Configure a production-ready database (MySQL).
- Manage static files and templates efficiently.
- Deploy a Django application to a cloud provider (Render).

## 🛠️ Prerequisites

Before starting, ensure you have:
- **Python 3.8+** installed.
- **Git** for version control.
- **MySQL** installed and running locally (optional, but recommended for this module).

---

## 🔄 Traditional Development Workflow

In this project, we follow a **Traditional Development Workflow**. This ensures a logical flow of data from the database to the user interface.

**The Order of Operations:**
1.  **Models (`models.py`)**: Define the database structure first.
2.  **Forms (`forms.py`)**: Create forms based on models to handle user input.
3.  **Views (`views.py`)**: Write the logic to process data and forms.
4.  **Templates (`templates/`)**: Design the HTML pages to display data.
5.  **URLs (`urls.py`)**: Finally, map URLs to the views.

---

## 🚀 Step-by-Step Implementation Guide

Follow these steps to build the project from scratch. This mirrors the process we follow in the video lessons.

### Phase 1: Project Initialization

1.  **Create the Project Environment**
    We always start by isolating our dependencies.
    ```bash
    # Create virtual environment
    python -m venv .venv
    
    # Activate it
    # Windows:
    .venv\Scripts\activate
    # Mac/Linux:
    source .venv/bin/activate
    ```

2.  **Install Django & Drivers**
    We need Django and the MySQL driver.
    ```bash
    pip install django mysqlclient
    ```

3.  **Start the Project**
    ```bash
    django-admin startproject BlogProject
    cd BlogProject
    ```

### Phase 2: App Architecture

In professional Django development, we split functionality into separate "apps". For this blog, we need three:

1.  **Create the Apps**
    ```bash
    python manage.py startapp blogapp      # Handles posts
    python manage.py startapp authorapp    # Handles user profiles
    python manage.py startapp categoryapp  # Handles post categories
    ```

2.  **Register Apps**
    Go to `BlogProject/settings.py` and add them to `INSTALLED_APPS`. This tells Django they exist.
    ```python
    INSTALLED_APPS = [
        # ... default apps ...
        'blogapp',
        'authorapp',
        'categoryapp',
    ]
    ```

### Phase 3: Database Setup (MySQL)

We are switching from SQLite to MySQL for better scalability.

1.  **Update `settings.py`**
    Replace the `DATABASES` configuration:
    ```python
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'blog_db',
            'USER': 'root',       # Your MySQL username
            'PASSWORD': 'password', # Your MySQL password
            'HOST': 'localhost',
            'PORT': '3306',
        }
    }
    ```
2.  **Create the Database**
    Log in to your MySQL shell and run:
    ```sql
    CREATE DATABASE blog_db;
    ```

### Phase 4: Implementation Progress

We are currently building the core functionality following our workflow.

#### 1. Models (`models.py`)
We have defined the data structures for our apps:
-   **Author**: Name, Email, Phone, Bio, Age.
-   **Category**: Name, Description.
-   **Blog**: Title, Content, Created At, Author (FK), Category (FK).

#### 2. Forms (`forms.py`)
We created `ModelForm`s for each model to simplify data entry.
-   Used `fields = '__all__'` to include all model fields automatically.

#### 3. Views & Templates
-   **Author App**:
    -   `home`: Displays the list of authors (`authorlist.html`).
    -   `add_author`: Handles adding new authors.

#### 4. URL Configuration
We routed traffic from the main project to our individual apps.

1.  **Update Main `urls.py`**
    In `BlogProject/urls.py`, use `include()` to delegate URLs.
    ```python
    from django.urls import path, include

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('blog/', include('blogapp.urls')),
        path('author/', include('authorapp.urls')),
        path('category/', include('categoryapp.urls')),
    ]
    ```

2.  **Create App URLs**
    We are creating `urls.py` files for each app as we implement their views.

---

## ☁️ Deployment (Render)

Ready to show the world? Let's deploy to Render.

### 1. Production Prep
Create a `requirements.txt` and `build.sh` file in the root directory.

**`build.sh`**:
```bash
#!/usr/bin/env bash
set -o errexit
pip install -r requirements.txt
cd BlogProject
python manage.py collectstatic --no-input
python manage.py migrate
```

### 2. Render Configuration
1.  Push to GitHub.
2.  Create a new **Web Service** on Render.
3.  **Build Command**: `./build.sh`
4.  **Start Command**: `cd BlogProject && gunicorn BlogProject.wsgi:application`
5.  **Environment Variables**: Add `PYTHON_VERSION` = `3.9.0` (or your version).

---

## 📚 Resources
- [Django Official Documentation](https://docs.djangoproject.com/)
- [Render Deployment Guide](https://render.com/docs/deploy-django)

Happy Coding! 🚀

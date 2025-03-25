# Task Management API

This is a Django REST Framework-based API for managing tasks, allowing users to create tasks, assign them to users, and retrieve assigned tasks.

## 🚀 Features
- ✅ Create a new task
- ✅ Assign a task to one or multiple users
- ✅ Retrieve tasks assigned to a specific user

## 📌 Installation & Setup
- create a virtual environment 
- install dependencies 
- apply migrations and start the Django server
- make API requests to create task, assign a task and fetch the task

## 📌 FOLDER STRUCTURE

task_management/
│-- tasks/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── urls.py
│   ├── views.py
│-- task_management/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│-- manage.py
│-- README.md


## 📌 Sample API Requests

    ### 1️⃣ Create a task:
        curl -X POST http://127.0.0.1:8000/tasks/create/ \
     -H "Content-Type: application/json" \
     -d '{"name": "Fix Security Issues", "description": "Resolve vulnerabilities in system"}'

    ### 2️⃣ Assign a task:
        curl -X POST http://127.0.0.1:8000/tasks/1/assign/ \
     -H "Content-Type: application/json" \
     -d '{"user_id": 2}'

    ### 3️⃣ Get Tasks for a User
        curl -X GET http://127.0.0.1:8000/tasks/user/2/tasks/


### Clone the Repository
```bash
git clone https://github.com/aanyas_24/Django-Project---JOSH.git
cd Django-Project---JOSH

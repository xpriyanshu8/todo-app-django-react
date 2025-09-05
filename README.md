# Fullstack To-Do App (Django + React)

## 🚀 Project Overview
A fullstack To-Do application built with Django REST Framework (backend) and React (frontend).  
Features:
- JWT Authentication (Login/Logout)
- CRUD (Create, Read, Update, Delete) tasks
- Filtering, Searching, Sorting
- Pagination
- CORS enabled
- Local deployment on Windows

## 🛠 Tech Stack
- Backend: Django, Django REST Framework
- Frontend: React, Axios
- Database: SQLite (local)
- Auth: JWT (SimpleJWT)

## ⚡ Features
- Add new tasks
- Mark complete/incomplete
- Delete tasks
- Search & filter tasks
- Pagination for large lists
- User authentication with JWT

## 📂 Project Setup
### Backend (Django)
```bash
cd backend
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

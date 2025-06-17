
# 📝 ToDo List API

A simple RESTful ToDo List API built with **Django** and **Django REST Framework**, featuring **JWT authentication** and user-specific task management. 
---

## 🚀 Features

- ✅ User Registration
- ✅ JWT Authentication (Login with Access/Refresh Tokens)
- ✅ CRUD operations for ToDos:
  - Create, View, Update, Delete
- ✅ Only authenticated users can manage their own ToDos
- ✅ Boolean field to mark ToDos as completed

---

## 🛠 Tech Stack

- Python 3
- Django
- Django REST Framework
- SimpleJWT (for JWT Auth)


---

## 🔐 Authentication

Authentication is handled via **JSON Web Tokens (JWT)**.

### 1. Register a user
```
POST /api/register/
```

### 2. Obtain JWT token
```
POST /api/token/
{
  "username": "your_username",
  "password": "your_password"
}
```

### 3. Use the token in Postman or any client:

```
Key: Authorization
Value: Bearer your_access_token
```

---


## 📦 Setup Instructions

1. **Clone the repository**

```bash
git clone https://github.com/your-username/To-Do-List-Api.git
cd To-Do-List-Api
```

2. **Create a virtual environment & activate it**

```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Run migrations and start server**

```bash
python manage.py migrate
python manage.py runserver
```

---

## 🗓 ToDo Features in Progress

- [ ] Filtering, searching, and ordering
- [ ] Task prioritization or due dates
- [ ] Testing with Django's test client or pytest
- [ ] Optional UI with Django Templates or React

---

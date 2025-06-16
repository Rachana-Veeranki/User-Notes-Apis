# 📝 User Notes API

A REST API for user registration, login (token-based), and secure note management, built using Django REST Framework and PostgreSQL.

---

## 🚀 Features

- User registration (no auth needed)
- Token-based user login
- Secure CRUD operations on personal notes
- Only authenticated users can access their notes
- Modular and scalable code structure
- Postman collection included

---

## 🛠️ Technologies Used

- Python 3.10+
- Django 4.x
- Django REST Framework
- PostgreSQL
- Token Authentication

---

## ⚙️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/Rachana-Veeranki/User-Notes-Apis.git
cd User-Notes-Apis


2. Create and activate virtual environment

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate


3. Install dependencies

pip install -r requirements.txt

4. Configure PostgreSQL database in notes_api/settings.py

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'notes_db',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

5. Run migrations

python manage.py makemigrations
python manage.py migrate

6. Start the development server

python manage.py runserver

🔐 API Endpoints

🔓 Public Endpoints

| Method | Endpoint     | Description         | Auth Required |
| ------ | ------------ | ------------------- | ------------- |
| POST   | `/register/` | Register a new user | ❌ No          |
| POST   | `/login/`    | Login and get token | ❌ No          |


📝 Notes Endpoints (Protected)

| Method | Endpoint       | Description         | Auth Required |
| ------ | -------------- | ------------------- | ------------- |
| GET    | `/notes/`      | List all user notes | ✅ Yes         |
| POST   | `/notes/`      | Create a new note   | ✅ Yes         |
| PUT    | `/notes/<id>/` | Update a note by ID | ✅ Yes         |
| DELETE | `/notes/<id>/` | Delete a note by ID | ✅ Yes         |


🛡 Add the following header for all authenticated requests:

Authorization: Token your_token_here

📬 Postman Collection

📁 Notes_Apis.postman_collection.json
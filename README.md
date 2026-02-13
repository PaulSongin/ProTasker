# ProTasker - Task Management API

A Full-stack Task Management System built with **FastAPI**, **PostgreSQL**, and **SQLAlchemy**. This project demonstrates modern Python development practices, including OOP, REST API design, and database relationships.

## 🚀 Features
- **User Authentication**: Secure registration and login using JWT and password hashing (bcrypt).
- **Task Management**: Full CRUD operations for tasks linked to specific users.
- **Relational Database**: PostgreSQL with One-to-Many relationships.
- **Auto-generated Documentation**: Interactive API docs via Swagger UI.

## 🛠 Tech Stack
- **Backend**: Python 3.x, FastAPI
- **Database**: PostgreSQL, SQLAlchemy (ORM)
- **Validation**: Pydantic
- **Security**: Passlib, Jose (JWT)
- **Frontend**: HTML, CSS, JavaScript (Vanilla)

## 🔧 Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/protasker.git
   cd protasker
Set up a virtual environment:
code
Bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install dependencies:
code
Bash
pip install -r requirements.txt
Environment Variables:
Create a .env file and add your database credentials:
code
Env
DATABASE_URL=postgresql://postgres:password@localhost:5432/protasker_db
SECRET_KEY=your_secret_key
Run the application:
code
Bash
uvicorn app.main:app --reload
Access the API at http://127.0.0.1:8000 and Swagger docs at /docs.

🧪 Testing

Run tests using pytest:

pytest
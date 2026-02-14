# ProTasker — Full-Stack Task Management System

A professional Task Management application built with **Python 3.13**, featuring an asynchronous **FastAPI** backend, a **PostgreSQL** relational database, and an interactive **JavaScript** frontend.

This project was developed to demonstrate modern software engineering patterns, including **DAO (Data Access Object)**, **Dependency Injection**, and **Automated Testing**.

## 🚀 Key Features

- **User Authentication**: Secure registration with password hashing using the `bcrypt` algorithm.
- **Task Management (CRUD)**: Create and retrieve tasks linked to specific user accounts (One-to-Many relationship).
- **Asynchronous API**: Built with FastAPI for high performance and scalability.
- **Data Validation**: Strict data typing and validation using **Pydantic V2**.
- **Responsive UI**: A clean, modern frontend built with **Bootstrap 5** and **Vanilla JavaScript (Fetch API)**.
- **Automated Testing**: Comprehensive test suite with **Pytest**.

## 🛠 Tech Stack

- **Backend**: Python 3.13, FastAPI
- **Database**: PostgreSQL
- **ORM**: SQLAlchemy 2.0
- **Security**: Bcrypt (Password Hashing)
- **Testing**: Pytest, HTTPX
- **Frontend**: HTML5, CSS3, JavaScript (ES6), Bootstrap 5

## 🔧 Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/ProTasker.git
cd ProTasker
2. Set up a virtual environment
code
Bash
python -m venv .venv
# On Windows:
.venv\Scripts\activate
# On macOS/Linux:
source .venv/bin/activate
3. Install dependencies
code
Bash
pip install -r requirements.txt
4. Database Configuration
Create a .env file in the root directory and add your PostgreSQL credentials:
code
Env
DATABASE_URL=postgresql://postgres:YOUR_PASSWORD@localhost:5432/protasker_db
5. Run the application
code
Bash
uvicorn app.main:app --reload
The app will be available at: http://127.0.0.1:8000
📖 API Documentation
FastAPI automatically generates interactive documentation. Once the server is running, you can access:
Swagger UI: http://127.0.0.1:8000/docs
ReDoc: http://127.0.0.1:8000/redoc
🧪 Running Tests
To run the automated test suite, use the following command:
code
Bash
python -m pytest
📁 Project Structure
code
Text
ProTasker/
├── app/
│   ├── main.py          # Application entry point & API routes
│   ├── models.py        # SQLAlchemy database models
│   ├── schemas.py       # Pydantic data schemas (Validation)
│   ├── crud.py          # Database CRUD operations (DAO Pattern)
│   ├── database.py      # Database connection & session setup
│   ├── utils.py         # Helper functions (Hashing)
│   ├── static/          # Static files (CSS, JS)
│   └── templates/       # HTML templates (Jinja2)
├── tests/               # Pytest test suite
├── .env                 # Environment variables (private)
├── .gitignore           # Git ignore rules
└── requirements.txt     # Project dependencies
📝 Contact
Developed by Pavel Songin — Feel free to contact me for internship opportunities!

email: songinpavel2006@gmail.com
linkedin: https://www.linkedin.com/in/paul-songin-a04194364/
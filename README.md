# 🎓 Campus Portal

A Django-based web application for managing campus events, announcements, and student activities. This platform helps students stay updated and interact with campus services efficiently.

---

## 🚀 Live Demo

👉 https://campusportal-7q41.onrender.com

---

## 📌 Features

✨ User Authentication (Login / Register)
✨ Event Registration System
✨ Announcements Section
✨ Contact Form for Student Queries
✨ Responsive UI Design
✨ Static Files Handling with WhiteNoise

---

## 🛠️ Tech Stack

* **Backend:** Django (Python)
* **Frontend:** HTML, CSS
* **Database:** SQLite (Development)
* **Deployment:** Render
* **Version Control:** Git & GitHub

---

## 📂 Project Structure

```
campusportal/
│
├── campusportal/        # Project settings
├── myapp/               # Main app
│   ├── templates/
│   ├── static/
│   ├── models.py
│   ├── views.py
│   └── urls.py
│
├── manage.py
├── requirements.txt
└── .gitignore
```

---

## ⚙️ Installation (Local Setup)

1. Clone the repository:

```bash
git clone https://github.com/jeni-g/campusportal.git
cd campusportal
```

2. Create virtual environment:

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run migrations:

```bash
python manage.py migrate
```

5. Start server:

```bash
python manage.py runserver
```

---

## 🌐 Deployment

This project is deployed using **Render**:

* Build Command:

```bash
pip install -r requirements.txt && python manage.py migrate && python manage.py collectstatic --noinput
```

* Start Command:

```bash
gunicorn campusportal.wsgi
```

---

## 🧠 Learning Outcomes

✔ Built a full-stack Django web application
✔ Implemented authentication system
✔ Managed static files in production
✔ Deployed project using Render
✔ Debugged real-world deployment issues

---

## 🔮 Future Improvements

🚀 Add PostgreSQL database
🚀 Improve UI with animations
🚀 Add Admin Dashboard enhancements
🚀 Implement REST API

---

## 👩‍💻 Author

**Jeni G**
Engineering Student

---

## ⭐ Show your support

If you like this project, give it a ⭐ on GitHub!

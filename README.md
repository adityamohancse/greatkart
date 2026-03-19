# 🛒 GreatKart - Django E-Commerce Web Application

🚀 Live Demo: https://adityamohan.pythonanywhere.com

---

## 📌 Overview

GreatKart is a **production-ready e-commerce backend system** built using Django and Django REST Framework (DRF). The project focuses on designing scalable backend architecture and implementing core functionalities such as authentication, product management, cart operations, and order processing.

The system demonstrates practical backend engineering concepts including RESTful API design, database optimization using filtering and pagination, and a modular application structure for maintainability.

This project reflects a strong foundation in **backend development, API design, and system scalability**, aligned with industry-level software engineering practices.

---

## ✨ Features

- 🔐 User Registration & Login System
- 🛍️ Product Listing & Categories
- 🛒 Add to Cart Functionality
- 💳 Checkout & Billing System
- 📦 Order Management
- 📧 Email Verification System
- 🧑‍💼 Django Admin Panel for Backend Management
- 🔍 Product Search Feature
- ⭐ Ratings & Reviews System

---

## 🖥️ Live Demo

👉 https://adityamohan.pythonanywhere.com

---

## 📸 Screenshots

### 🏠 Home Page
![Home](greatkart/screenshots/home.png)

---

### 📦 Product Page
![Product](greatkart/screenshots/product.png)

---

### 🛒 Cart Page
![Cart](greatkart/screenshots/cart.png)

---

### 💳 Billing Page
![Billing](greatkart/screenshots/billing.png)

---

## 🛠️ Tech Stack

- **Backend:** Django (Python)
- **Frontend:** HTML, CSS, Bootstrap
- **Database:** SQLite (Production-ready for PostgreSQL)
- **Authentication:** Django Auth System
- **Deployment:** PythonAnywhere

---

## ⚙️ Installation & Setup

```bash
# Clone repository
git clone https://github.com/adityamohancse/greatkart.git

# Navigate into project
cd greatkart

# Create virtual environment
python -m venv venv

# Activate environment
venv\Scripts\activate   # Windows
source venv/bin/activate  # Linux/Mac

# Install dependencies
pip install -r requirements.txt

# Apply migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Run server
python manage.py runserver

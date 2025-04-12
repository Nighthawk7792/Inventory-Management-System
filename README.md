# Inventory Management System

![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![Bootstrap](https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white)

A full-featured inventory management system built with Django and Bootstrap for tracking products, stock levels, and inventory value.

## Features

- 📦 Product catalog management
- 🔢 Stock level tracking
- 💰 Inventory value calculation
- 📊 Basic reporting
- 👤 User authentication (admin only)
- ✅ CRUD operations for inventory items

## Installation

### Prerequisites
- Python 3.8+
- pip package manager

### Setup
1. Clone the repository:
   ```bash
   Create and activate virtual environment:

bash
Copy
python -m venv venv
# Windows:
.\venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate
Install dependencies:

bash
Copy
pip install -r requirements.txt
Set up the database:

bash
Copy
python manage.py migrate
Create admin user:

bash
Copy
python manage.py createsuperuser
Usage
Start the development server:

bash
Copy
python manage.py runserver
Access the application:

Main interface: http://localhost:8000

Admin panel: http://localhost:8000/admin

Default test credentials (if using sample data):

Username: admin

Password: admin123

Project Structure
Copy
Inventory-Management-System/
├── inventory/          # Project configuration
├── items/              # Inventory app
│   ├── migrations/     # Database migrations
│   ├── templates/      # HTML templates
│   ├── admin.py        # Admin configuration
│   ├── models.py       # Data models
│   ├── views.py        # Application logic
│   └── urls.py         # URL routing
├── templates/          # Base templates
├── static/             # CSS/JS assets
├── manage.py           # Django CLI
└── requirements.txt    # Dependencies
Screenshots
Item List
Inventory item listing view

Add Item
Add new item form

Troubleshooting
If you encounter issues:

Verify all migrations are applied:

bash
Copy
python manage.py makemigrations
python manage.py migrate
Check for port conflicts:

bash
Copy
python manage.py runserver 8001
Reset the database (development only):

bash
Copy
rm db.sqlite3
python manage.py migrate
Contributing
Fork the repository

Create your feature branch (git checkout -b feature/AmazingFeature)

Commit your changes (git commit -m 'Add some AmazingFeature')

Push to the branch (git push origin feature/AmazingFeature)

Open a Pull Request
   git clone https://github.com/Nighthawk7792/Inventory-Management-System.git
   cd Inventory-Management-System# Inventory-Management-System

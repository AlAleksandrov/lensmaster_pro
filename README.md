# 📷 LensMaster Pro  
  
**LensMaster Pro** is a professional Django web application designed for photography and videography studios. It features a curated portfolio, service package management, client booking requests, and a studio equipment inventory system.  
  
---  
  
## ✨ Key Features & Architecture  
  
- **Multi-app Django Architecture**: Clean separation of concerns between **Bookings**, **Productions**, **Inventory**, and **Common** utilities.  
- **Full CRUD Functionality**: Complete management systems for **Productions** and **Service Packages** (Create, Read, Update, Delete).  
- **Dynamic Portfolio**: Categorized project showcase with detailed production pages and related items.  
- **Client Booking System**: Integrated booking request forms with robust server-side validation.  
- **Inventory Tracking**: Professional equipment management with auto-generated internal inventory IDs.  
- **Production Ready**: PostgreSQL integration via environment variables and custom 404 error handling.  
  
---  
  
## 🗂️ Directory Structure  
  
```text  
lensmaster_pro/  
|-- bookings/          # Service packages & client booking requests  
|-- productions/       # Portfolio categories & project showcases  
|-- inventory/         # Studio equipment & gear tracking  
|-- common/            # Shared abstract models, mixins & utilities  
|-- lensmaster_pro/    # Core project configuration (settings, urls)  
|-- static/            # Global CSS, JavaScript, and images  
`-- templates/         # HTML templates organized by application module  

🧭 Site Map & Operations
Feature / Page	URL Route	Operations	Description
Home	/	View	Featured categories and latest studio work.
Portfolio	/portfolio/	View	Browse all categories and productions.
Productions	/productions/	Full CRUD	Detailed project views and management.
Service Packages	/bookings/packages/	Full CRUD	List and manage photography/video tiers.
Booking Request	/bookings/request/	Create	Client intake form with validation.
Inventory	/inventory/	View	Internal list of studio gear grouped by type.
404 Error	-	-	Custom-designed "Page Not Found" handler.
🚀 Installation & Setup
1) Clone the repository

bash
Copy
git clone https://github.com/AlAleksandrov/lensmaster_pro  
cd lensmaster_pro  

2) Create and activate a virtual environment

bash
Copy
python -m venv .venv  
  
# Windows:  
.venv\Scripts\activate  
  
# macOS/Linux:  
source .venv/bin/activate  

3) Install dependencies

bash
Copy
pip install -r requirements.txt  

4) Configure environment variables

Create a .env file in the project root (next to manage.py):

env
Copy
SECRET_KEY=your-secret-key-here  
DEBUG=True  
ALLOWED_HOSTS=127.0.0.1,localhost  
  
DB_ENGINE=django.db.backends.postgresql  
DB_NAME=lensmaster_pro  
DB_USER=postgres  
DB_PASSWORD=your_password  
DB_HOST=127.0.0.1  
DB_PORT=5432  
  
LANGUAGE_CODE=en-us  
TIME_ZONE=UTC  
USE_I18N=True  
USE_TZ=True  

5) Apply migrations & Run

bash
Copy
# Run migrations  
python manage.py migrate  
  
# Start the server  
python manage.py runserver  

Open in your browser → http://127.0.0.1:8000/
🌐 Live Demo (optional)

A live demo may be available here (ngrok, temporary):

    Live Demo Link

If the link is inactive, please run the project locally following the steps above.
🖼️ Screenshots

Home page
Portfolio page
Production details
🧪 Data Management (via Django Admin)

Authentication for the public site is intentionally excluded (exam requirement). Use the admin panel to manage content:

    Create an admin user:

    bash
    Copy
    python manage.py createsuperuser  

    Access Admin Panel: http://127.0.0.1:8000/admin/
    Manage Content: Add Categories, Productions, Service Packages, and Equipment.

🧩 Custom 404 Page

To test the custom error page, set DEBUG=False in your .env file and visit a non-existent URL:

    http://127.0.0.1:8000/this-does-not-exist/

🗃️ Tech Stack

    Backend: Django (Python)
    Database: PostgreSQL
    Forms: django-crispy-forms with Bootstrap 5
    Environment: python-dotenv
    Images: Pillow

🧾 Project Notes

    Git History: Includes commits on multiple separate days as required.
    License: Educational project for the Django Basics Exam.
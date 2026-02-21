# 📷 LensMaster Pro    
    
**LensMaster Pro** is a Django web application built for a photography and videography studio.    
It presents a curated portfolio of productions, showcases service packages, handles booking    
requests from clients, and manages the studio's equipment inventory.    
    
---    
    
## ✨ Features    
    
- Multi-app Django project with clearly defined responsibilities per app    
- Full CRUD for **Productions** and **Service Packages**    
- Portfolio organised by categories with production detail pages    
- Booking request form with full server-side validation    
- Equipment inventory with auto-generated internal IDs    
- Template inheritance with a shared base layout and a custom 404 page    
- PostgreSQL database configured via environment variables    
    
---    
    
## 🗂️ Project Structure    
    
```text  
lensmaster_pro/  
├── bookings/ # Service packages & booking requests  
│ ├── forms.py  
│ ├── models.py  
│ ├── urls.py  
│ └── views.py  
├── common/ # Shared abstract mixins & utilities  
│ └── models.py  
├── inventory/ # Studio equipment inventory  
│ ├── models.py  
│ ├── urls.py  
│ └── views.py  
├── productions/ # Portfolio categories & productions  
│ ├── forms.py  
│ ├── models.py  
│ ├── urls.py  
│ └── views.py  
├── lensmaster_pro/ # Project configuration  
│ ├── settings.py  
│ └── urls.py  
├── static/  
│ ├── css/  
│ └── images/  
└── templates/  
├── base.html  
├── 404.html  
├── home.html  
├── bookings/  
│ ├── booking_form.html  
│ ├── booking_success.html  
│ ├── package_form.html  
│ └── package_list.html  
├── inventory/  
│ └── equipment_list.html  
└── productions/  
├── category_list.html  
├── production_confirm_delete.html  
├── production_detail.html  
├── production_form.html  
└── production_list.html  

📄 Main Pages
Page	Description
Home	Featured categories and latest productions
Portfolio / Categories	All categories with their productions
Productions by Category	Filtered list of productions per category
Production Detail	Full details + related productions
Production Create / Edit / Delete	Full CRUD for productions
Service Packages	List of available studio packages
Package Create / Edit / Delete	Full CRUD for service packages
Booking Request	Client-facing booking form with validation
Booking Success	Confirmation page after booking
Equipment Inventory	Equipment list grouped by type
404	Custom not found page
🗄️ Database Models & Relationships

    Category — portfolio category (slug, description, cover image)
    Production — portfolio item linked to a Category (Many-to-One)
    Production ↔ Equipment — equipment used in a production (Many-to-Many)
    ServicePackage — studio service offering linked to a Category (Many-to-One)
    BookingRequest — client booking linked to a ServicePackage (Many-to-One)
    Equipment — studio gear with auto-generated inventory ID

⚙️ Installation & Setup
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

5) Set up the PostgreSQL database

sql
Copy
CREATE DATABASE lensmaster_pro;    

6) Apply migrations

bash
Copy
python manage.py migrate    

7) Run the development server

bash
Copy
python manage.py runserver    

Open in your browser → http://127.0.0.1:8000/
🔧 Admin Panel (Optional)

To manage content through the Django admin interface:

bash
Copy
python manage.py createsuperuser    

Then open → http://127.0.0.1:8000/admin/
📁 Static & Media

    Static files are located in static/
    Uploaded media (cover images, etc.) is stored in media/ (auto-created on first upload)

🛠️ Tech Stack
Technology	Purpose
Django	Web framework
PostgreSQL	Database
django-crispy-forms	Form rendering
crispy-bootstrap5	Bootstrap 5 form styling
Pillow	Image handling
python-dotenv	Environment variable management
📝 License

Educational project — Django Basics Exam.

# 📷 LensMaster Pro

**LensMaster Pro** is a professional Django web application designed for photography and videography studios. It features a curated portfolio, service package management, client booking requests, and a studio equipment inventory system.

---

## ✨ Key Features

- **Multi-app Architecture**: Clean separation of concerns (Bookings, Productions, Inventory, Common).
- **Full CRUD Functionality**:
  - **Productions**: Create, View, Update, and Delete portfolio items.
  - **Service Packages**: Full management of studio offerings (Create, View, Update, Delete).
- **Dynamic Portfolio**: Organized by categories with detailed production pages and related items.
- **Booking System**: Client-facing booking form with robust server-side validation.
- **Inventory Management**: Equipment tracking with auto-generated internal inventory IDs.
- **Custom 404 Page**: User-friendly error handling for missing resources.
- **PostgreSQL Integration**: Database configuration via environment variables.

---

## 🗂️ Project Structure

```text
lensmaster_pro/
|-- bookings/                  # Service packages & booking requests
|   |-- forms.py
|   |-- models.py
|   |-- urls.py
|   `-- views.py
|-- common/                    # Shared abstract mixins & utilities
|   `-- models.py
|-- inventory/                 # Studio equipment inventory
|   |-- models.py
|   |-- urls.py
|   `-- views.py
|-- productions/               # Portfolio categories & productions
|   |-- forms.py
|   |-- models.py
|   |-- urls.py
|   `-- views.py
|-- lensmaster_pro/            # Project configuration
|   |-- settings.py
|   `-- urls.py
|-- static/
|   |-- css/
|   `-- images/
`-- templates/
    |-- base.html
    |-- 404.html
    |-- home.html
    |-- bookings/
    |   |-- booking_form.html
    |   |-- booking_success.html
    |   |-- package_form.html
    |   `-- package_list.html
    |-- inventory/
    |   `-- equipment_list.html
    `-- productions/
        |-- category_list.html
        |-- production_confirm_delete.html
        |-- production_detail.html
        |-- production_form.html
        `-- production_list.html
```

---

## 📄 Main Pages & CRUD Operations

| Feature | Description | CRUD Status |
|---|---|---|
| **Home** | Featured categories and latest studio work. | View |
| **Portfolio** | Browse all categories and their respective productions. | View |
| **Productions** | Detailed view of specific projects with related items. | **Full CRUD** |
| **Service Packages** | List of available photography/videography packages. | **Full CRUD** |
| **Booking Request** | Client form to request a session with validation. | Create |
| **Inventory** | Internal list of studio gear grouped by type. | View |
| **404 Error** | Custom-designed "Page Not Found" template. | - |

---

## ⚙️ Installation & Setup

### 1) Clone the repository

```bash
git clone https://github.com/AlAleksandrov/lensmaster_pro
cd lensmaster_pro
```

### 2) Create and activate a virtual environment

```bash
python -m venv .venv

# Windows:
.venv\Scripts\activate

# macOS/Linux:
source .venv/bin/activate
```

### 3) Install dependencies

```bash
pip install -r requirements.txt
```

### 4) Configure environment variables

Create a `.env` file in the project root (next to `manage.py`):

```env
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
```

### 5) Apply migrations

```bash
python manage.py migrate
```

### 6) Run the development server

```bash
python manage.py runserver
```

Open in your browser → **http://127.0.0.1:8000/**

---

## 🛠️ Tech Stack

- **Backend**: Django (Python)
- **Database**: PostgreSQL
- **Forms**: django-crispy-forms with Bootstrap 5
- **Environment**: python-dotenv
- **Images**: Pillow

---

## 📝 License

Educational project for the Django Basics Exam.

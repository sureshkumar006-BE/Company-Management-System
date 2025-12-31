Company-Data-Manager

A Python Django REST Framework–based application for managing company records with full CRUD operations, strict field validations, and paginated REST APIs.

🚀 Project Overview

Company-Data-Manager is a backend RESTful service developed using Python and Django REST Framework (DRF).
It allows users to create, retrieve, update, delete, and list company records while enforcing business rules and data integrity through validations.

🛠️ Tech Stack

Python

Django

Django REST Framework (DRF)

SQLite / PostgreSQL (configurable)

REST API

Git

📦 Features

Create company records

Update company details

Delete company records

Retrieve company by ID

Retrieve all companies with pagination

Strong field-level validations

RESTful API architecture

Clean and modular code structure

🗂️ Entity Details & Validations
Field	Description
Id	Auto-generated primary key
Company Name	Mandatory, minimum 5 characters, non-empty
Email ID	Mandatory, valid email format
Company Code	Unique, optional, 5-character format (AA12E / AA12N)
Strength	Optional, zero or positive integer
Website	Optional, valid URL
Created Time	Mandatory, auto-generated date & time
🔗 API Endpoints
Method	Endpoint	Description
POST	/api/companies/	Create a company
GET	/api/companies/	Get all companies (paginated)
GET	/api/companies/{id}/	Get company by ID
PUT	/api/companies/{id}/	Update company
DELETE	/api/companies/{id}/	Delete company
⚙️ Installation & Setup
1️⃣ Clone the Repository
git clone https://github.com/your-username/Company-Data-Manager.git
cd Company-Data-Manager

2️⃣ Create Virtual Environment
python -m venv venv
source venv/bin/activate   # Linux / Mac
venv\Scripts\activate      # Windows

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Apply Migrations
python manage.py migrate

5️⃣ Run the Server
python manage.py runserver

📌 Pagination

Pagination is enabled for the Get All Companies API.

Default page size can be configured in settings.py.

🧪 Testing

APIs can be tested using:

Postman

Swagger (if enabled)

Browser (GET requests)

📁 Project Structure (Simplified)
Company-Data-Manager/
│
├── company_app/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│
├── CompanyDataManager/
│   ├── settings.py
│   ├── urls.py
│
├── manage.py
├── requirements.txt
└── README.md

✅ Coding Standards

REST best practices followed

Clean and readable code

DRF serializers for validation

Proper HTTP status codes used

📄 License

This project is developed for learning and demonstration purposes.

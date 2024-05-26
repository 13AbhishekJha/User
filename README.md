## User Project

### The /User endpoint is available at https://tempname.pythonanywhere.com/api/users/

This project is a Django-based REST API for managing user data with attributes like ID, First Name, Last Name, Company Name, Age, City, State, Zip, Email, and Web.
Setup
Local Setup
Prerequisites

    Python 3.8 or higher
    Django
    Django REST framework
    Git

### Steps

    Clone the Repository
    git clone https://github.com/yourusername/User.git
    cd User

Create and Activate Virtual Environment

    python -m venv myvenv
    source myvenv/bin/activate

Install Dependencies

    pip install -r requirements.txt
    
Apply Migrations

    python manage.py migrate

Run the Server

    python manage.py runserver

Access the API
      
    Open your browser and navigate to http://127.0.0.1:8000/api/users


### API Endpoints
List Users

GET /api/users

    Response:
    [
      {
        "id": 1,
        "first_name": "James",
        "last_name": "Butt",
        "company_name": "Benton, John B Jr",
        "city": "New Orleans",
        "state": "LA",
        "zip": 70116,
        "email": "jbutt@gmail.com",
        "web": "http://www.bentonjohnbjr.com",
        "age": 70
      },
      ...
    ]

    Query Parameters:
        page: Page number for pagination.
        limit: Number of items per page (default is 5).
        name: Search by name (substring matching, case-insensitive).
        sort: Attribute to sort by (prefix with - for descending order).

Create User

POST /api/users

    Request Payload:
    {
      "id": 2,
      "first_name": "Josephine",
      "last_name": "Darakjy",
      "company_name": "Chanay, Jeffrey A Esq",
      "city": "Brighton",
      "state": "MI",
      "zip": 48116,
      "email": "josephine_darakjy@darakjy.org",
      "web": "http://www.chanayjeffreyaesq.com",
      "age": 48
    }

Response:

    {"User created successfully"}

Retrieve User

GET /api/users/{id}

    Response:
    {
      "id": 1,
      "first_name": "James",
      "last_name": "Butt",
      "company_name": "Benton, John B Jr",
      "city": "New Orleans",
      "state": "LA",
      "zip": 70116,
      "email": "jbutt@gmail.com",
      "web": "http://www.bentonjohnbjr.com",
      "age": 70
    }

Update User

PUT /api/users/{id}

    Request Payload:
    {
      "first_name": "Josephine",
      "last_name": "Darakjy",
      "age": 48
    }

Response:

    {"User updated successfully"}

Delete User

DELETE /api/users/{id}

    Response:

    {"User deletion successfully"}

### Running Tests

    To run the unit tests for the API endpoints, use the following command:
    
    python manage.py test

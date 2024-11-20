# QuizBit API
A Django-based project to provide a simplified API and database structure for QuizBit functionalities.

# Technologies Used
   - Django: Web framework for backend development.
   - Django REST Framework (DRF): For building RESTful APIs.
   - Database: PostgreSQL.
   - Postman: Used for testing and documenting APIs.

# Setup Instructions:
1. Clone Repository
   ```
   git clone https://github.com/YasinRafin/QuizBit_API.git
   cd QuizBit_API
   ```
2. Create a Virtual Environment
   ```
   python3 -m venv env
   source env/bin/activate 
   ```
3. Install Dependencies
   ```
   pip install -r requirements.txt

   ```
4. Setup Database settings in quizbit/settings.py
   ```
     DATABASES = {
      'default': {
          'ENGINE': 'django.db.backends.postgresql',
          'NAME': 'database_name',
          'USER': 'postgress_username',
          'PASSWORD': 'postgress_password',
          'HOST': 'localhost',
          'PORT': '5432',
      }
   }
   ```
5. Apply migrations
   ```
    python manage.py makemigrations
    python manage.py migrate

   ```
6. Create a Superuser
   ```
   python manage.py createsuperuser

   ```
7. Run the server
   ```
   python manage.py runserver
   ```
# API Endpoints
| Endpoint         |  Method          | Description                       |
|------------------|------------------|---------------------------------- |
| /question/questions/	 |   GET	    | Retrieve a list of all questions. |
| /question/questions/:id/	 |   GET	    | Get details of a specific question.  |
| /question/questions/:id/submit/ |	POST	| Submit an answer to a question.   |
| /question/users/:user_id/history/ |	GET	| Retrieve a user's practice history.  |

# Testing APIs with Postman:

To test the APIs:

  1. Open Postman.
  2. Import the Postman collection:
       - File: [Download](QuizBit API.postman_collection.json)
       - This file contains pre-configured requests for all API endpoints.
  3. Adjust parameters (e.g., question ID, user ID) as needed.
  4. Click Send to test each API.

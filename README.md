\# Book Management API



A RESTful Book Management API built with \*\*Python, FastAPI, SQLAlchemy, and SQLite\*\*. The application allows users to create, retrieve, update, and delete book records through HTTP endpoints.



\## Features



\- Create new book records.

\- Retrieve all available books.

\- Retrieve individual books by ID.

\- Update existing book records.

\- Delete book records.

\- Validate incoming data using Pydantic.

\- Persist records using SQLAlchemy and SQLite.

\- Handle missing book records with appropriate HTTP 404 responses.

\- Interactive API documentation through Swagger UI.



\## Technologies Used



\- Python

\- FastAPI

\- SQLAlchemy

\- SQLite

\- Pydantic

\- Uvicorn



\## Project Structure



```text

Book-Management-API/

│

├── main.py

├── models.py

├── database.py

├── requirements.txt

├── .gitignore

└── README.md

```



\## Installation and Setup



\### 1. Clone the repository



```bash

git clone https://github.com/PSALMUEL-SAINT/Book-Management-API.git

cd Book-Management-API

```



\### 2. Create a virtual environment



```bash

python -m venv venv

```



\### 3. Activate the virtual environment



On Windows:



```bash

venv\\Scripts\\activate

```



\### 4. Install dependencies



```bash

pip install -r requirements.txt

```



\### 5. Start the application



```bash

uvicorn main:app --reload

```



The API will be available at:



`http://127.0.0.1:8000`



\## API Documentation



FastAPI provides interactive Swagger documentation at:



`http://127.0.0.1:8000/docs`



You can use Swagger UI to test all available endpoints.



\## API Endpoints



| Method | Endpoint | Description |

|---|---|---|

| GET | `/` | Welcome message |

| POST | `/books` | Create a book |

| GET | `/books` | Retrieve all books |

| GET | `/books/{book\_id}` | Retrieve a book by ID |

| PUT | `/books/{book\_id}` | Update a book |

| DELETE | `/books/{book\_id}` | Delete a book |



\## Book Data Example



Example JSON request for creating a book:



```json

{

&#x20; "title": "Deep Work",

&#x20; "author": "Cal Newport",

&#x20; "published\_year": 2016,

&#x20; "genre": "Productivity"

}

```



\## Learning Objectives



This project was developed to practise:



\- Building RESTful APIs with FastAPI.

\- Working with relational databases.

\- Using SQLAlchemy ORM for database operations.

\- Implementing CRUD functionality.

\- Validating data with Pydantic.

\- Managing database sessions through dependency injection.

\- Handling HTTP exceptions.



\## Future Improvements



\- User registration and authentication.

\- JWT-based access control.

\- PostgreSQL integration.

\- Automated testing with Pytest.

\- Docker containerisation.

\- API deployment.



\## Author



\*\*PSALMUEL-SAINT\*\*



GitHub: \[PSALMUEL-SAINT](https://github.com/PSALMUEL-SAINT)


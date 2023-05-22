
# FastAPI Project - Kimo.AI

Backend Server For Accessing Course Informations

## Author

Ajun Ravi

## Description

This is a basic FastAPI project for managing the course related informations.

## Features

- RESTful API endpoints to access courses and chapters information. Also a Post API to add user ratings against a chapter.
- Request validation using Pydantic models
- Automatic API documentation with Swagger UI

## Installation

1. Clone the repository:

   ```shell
   git clone https://github.com/ajunravi123/Kimo-CourseBackend
   cd Kimo-CourseBackend
Create a virtual environment (optional but recommended):

shell
Copy code
python -m venv venv
source venv/bin/activate  # for Unix/Linux
venv\Scripts\activate.bat  # for Windows
Install the dependencies:

shell
Copy code
pip install -r requirements.txt
Run the application:

shell
Copy code

Run "python migration.py" command to migrate the data from course.json to Local MongoDB. The script will take care of Database creation, making collections, adding indexes and migration processes.

To Run the App, execute the following command
uvicorn index:app --reload


Access the API documentation:

Open your web browser and navigate to http://localhost:8000/docs to view the Swagger UI documentation.


```sh
127.0.0.1:8000
```

Usage
Modify the routes/route.py file to define your API endpoints and logic.
Define Pydantic models in separate files or inline to validate request/response data.
Update the requirements.txt file if you add or remove dependencies.
Use pytest to validate the test cases. Which is in test_main.py file



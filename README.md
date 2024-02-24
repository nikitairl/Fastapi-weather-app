# FastAPI Weather App

This is a FastAPI application that periodically requests temperature and weather data from openweathermap.org via Celery's crontab periodic task for cities stored in the database. The requested temperature and all data are then stored in the database city model. FastAPI serves as an API with endpoints for adding a city and retrieving all cities from the database.

## Requirements

- Python 3.x
- FastAPI
- Uvicorn
- Celery
- SQLAlchemy
- Requests

## Installation

1. Clone the repository:

    ```bash
    https://github.com/nikitairl/Fastapi-weather-app.git
    cd Fastapi-weather-app
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Set up environment variables:
   
    Create a `.env` file in the project root directory and add the following variables:

    ```
    REDIS_URL=*your_redis_url*
    API_KEY=*your https://openweathermap.org/ api key*
    ```

## Usage

1. Start Celery worker and beat:

    ```bash
    celery --app app.worker.celery_app worker --beat -s celerybeat-schedule --loglevel INFO
    ```

2. Start the FastAPI application:

    ```bash
    uvicorn app.main:app --reload
    ```

3. Access the FastAPI Swagger documentation at `http://localhost:8000/docs` to interact with the API endpoints.


## Docker

SOON

## Notes

- Ensure that you have a valid API key from openweathermap.org and set it in the `.env` file.
- Adjust the Celery periodic task interval in `app.worker` as needed.
- This application uses SQLite as the default database. You can change it to another supported database by modifying the `DATABASE_URL` in the database.py file and installing the necessary dependencies (I will replace sqlite with postgresql and hide the url in .env soon).
- This README assumes a basic familiarity with FastAPI, Celery

Feel free to extend and modify the application as needed! If you have any questions or encounter any issues, please create an issue in the GitHub repository.

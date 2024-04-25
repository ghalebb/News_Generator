# News Collector Django Project

## Project Description

News Collector is a Django-based web application designed to aggregate news from various sources. This project can be easily set up on a local development environment or deployed using AWS Elastic Beanstalk.

## Prerequisites

Ensure you have Python installed on your machine. You can download Python from [python.org](https://www.python.org/downloads/). This project was developed using Python 3.8.x.

## Setup

### 1. Clone the Project
``` bash
 git clone https://github.com/ghalebb/News_Generator.git
 cd News_Generator
```
### 2. Install Dependencies

- Navigate to the project directory where `requirements.txt` is located.
- Run the following command to install the required Python packages:
  ```bash
  pip install -r requirements.txt
  ```

### 3. Configure the Project

- Navigate to the `news_collector` directory where `settings.py` is located.
- Modify the `DATABASES` setting to point to your local database. Use SQLite for development by default:
  ```python
  DATABASES = {
      'default': {
          'ENGINE': 'django.db.backends.sqlite3',
          'NAME': BASE_DIR / 'db.sqlite3',
      }
  }
  ```

### 4. Run Migrations

- Initialize the database and create necessary tables by running:
  ```bash
  python manage.py migrate
  ```

### 5. Run the Development Server

- Start the server with:
  ```bash
  python manage.py runserver
  ```
- Visit `http://127.0.0.1:8000/` in your browser to view the application.

## Deployment (AWS Elastic Beanstalk)

### 1. Prepare the Project

- Ensure that `.ebextensions` directory is correctly configured for deployment.

### 2. Deploy

- Follow the [official AWS documentation](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create-deploy-python-django.html) to deploy the Django application on Elastic Beanstalk.

## Contributing

Contributions to the News Collector project are welcome. Please ensure to follow standard coding conventions and submit pull requests for any enhancements.



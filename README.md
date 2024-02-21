# OC_Python_P10 | SoftDesk


Welcome to the GitHub repository of the SoftDesk API. This RESTful API is designed to provide a high-performance and secure backend, serving front-end applications on various platforms. Developed with Django and Django REST Framework (DRF), it meets modern requirements for security, performance, and sustainable development.

Getting Started
These instructions will help you get a copy of the project up and running on your local machine for development and testing purposes.

## Prerequisites
- Python 3.8+
- Poetry for dependency management

## Installation
Clone this repository to your local machine.
`git clone https://github.com/yourusername/softdesk-api.git`
Navigate to the project folder.
`cd softdesk-api`
Use Poetry to install the project dependencies.
`poetry install`
Activate the virtual environment.
`poetry shell`
Apply the migrations to set up the database.
`python manage.py migrate`
Start the development server.
`python manage.py runserver`

## Usage
Once the server is running, you can access the API at the following address: http://localhost:8000/api/

The API entry points include:

Users: Management of users, including registration, login, and profile management.  
Projects: Creation, modification, and consultation of projects.  
Issues: Management of issues related to projects, including creation, modification, and tracking.  

## Security
In accordance with OWASP and GDPR specifications, this API implements:

JWT Authentication for secure management of user sessions.
Role-based permissions to control access to the API's various resources.
Data protection to ensure the confidentiality and security of user information.
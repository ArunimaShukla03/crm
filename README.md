# Customer Management Application

A Django-based web application for managing customer information and orders.

## Features

- User authentication: Users can sign up, log in, and log out using their email and password. Password reset functionality is also available.
- Customer management: Users can create, view, update, and delete customer records. Each customer has a profile page with basic contact information and order history.
- Order management: Users can create, view, update, and delete orders for each customer. Orders have a status, date, and total amount.
- Search and filter: Users can search for customers by name, email, or phone number. Users can also filter customers by order status or date range.

## Tech Stack

- Python
- Django
- SQLite
- HTML
- Bootstrap
- Git
- GitHub

## Installation

To install and run the customer management application, follow these steps:

- Clone the GitHub repository: `git clone https://github.com/ArunimaShukla03/crm.git`
- Navigate to the project directory: `cd crm`
- Install the required dependencies: `pip install -r requirements.txt`
- Apply the migrations: `python manage.py migrate`
- Run the development server: `python manage.py runserver`
- Access the web application at [http://127.0.0.1:8000/](https://realpython.com/django-markdown/)

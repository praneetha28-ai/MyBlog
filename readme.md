# Django Blogging Website

This is a Django-based web application for a blogging website. It allows users to create and publish their own blog posts, while the admin has the ability to delete blogs by logging in.

## Technologies Used

- Django: The web framework used for developing the application.
- Python: The programming language used for the backend development.
- HTML/CSS: Used for the frontend presentation and styling.
- Bootstrap: CSS framework used for responsive and modern UI design.
- SQLite: The database management system used for storing blog data.

## Features

- User Registration: Users can create accounts and register to the website.
- User Authentication: Registered users can log in to access their account.
- Create and Publish Blogs: Authenticated users can create and publish their own blog posts.
- Blog Listing: Displays a list of published blogs on the website.
- Blog Details: Users can view the details of each blog, including the author, date, and content.
- Admin Dashboard: An admin panel is available for managing the website and deleting blogs.

## Setup Instructions

Clone the repository: git clone https://github.com/praneetha28-ai/MyBlog.git
Navigate to the project directory: cd newsapp
Create a virtual environment (optional but recommended): python -m venv venv
Activate the virtual environment:
On Windows: venv\Scripts\activate
On macOS/Linux: source venv/bin/activate
Install the project dependencies: pip install -r requirements.txt
Run the database migrations: python manage.py migrate
Start the development server: python manage.py runserver
Open your web browser and access the website at http://localhost:8000

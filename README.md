Authentication Project
This project is a simple Django-based authentication system that includes user registration, login, 
logout functionality, and a home page. It allows users to create accounts, authenticate themselves, and log out.

Features
User Registration: Allows users to register using Django's built-in UserCreationForm.
User Login: Users can log in using the AuthenticationForm and gain access to the home page.
User Logout: Logs the user out and redirects to the login page.
Home Page: Displays a welcome message with navigation options for registration and logout.

Technologies Used
Django: Web framework for building the project.
HTML: Basic templates for user interaction.
Django Auth: Built-in authentication for user management.
Installation

Clone the repository:
https://github.com/anageguchadze/authorization.git
cd auth_project

Install dependencies:
pip install -r requirements.txt

Apply migrations:
python manage.py migrate

Run the development server:
python manage.py runserver
Access the application: Open http://127.0.0.1:8000/ in your web browser.

File Structure
urls.py: Contains URL routing for different pages like login, register, and home.
views.py: Contains the views that render templates for registration, login, home, and logout functionality.
home.html: The welcome page for users after login.
register.html: The registration page for new users.
login.html: The login page for existing users.
logout.html: The logout page shown after logging out.
License

This project is licensed under the MIT License.

# Learning Flask Project

This is a beginner-friendly web application built with [Flask](https://flask.palletsprojects.com/) to demonstrate basic concepts like routing, template rendering, handling form submissions, and session management.

<p align="center">
  <img src="sc.png" width="400" alt="Login Page Screenshot">
</p>

## Project Structure

- **`app.py`**: The main entry point for the Flask application. It contains the server configuration, routing logic, and handles user authentication.
- **`templates/`**: Directory containing HTML templates rendered using Jinja2.
  - **`index.html`**: A basic login page with a form that takes a username and password.
  - **`welcome.html`**: A welcome dashboard shown to authenticated users, featuring a logout option.
- **`.env`**: Stores environment variables such as the secret key required for Flask session management.
- **`flask.txt`**: Contains quick learning notes on Flask routing, HTTP methods (GET/POST), and templating.
- **`rivision.py`**: *(Excluded from analysis)* Script containing additional revision or experimental code.

## Features

1. **User Authentication**:
   - Validates user credentials. Hardcoded for demonstration (`username: admin`, `password: 123`).
2. **Session Management**:
   - Utilizes Flask sessions to keep users logged in and securely log them out.
3. **Environment Variables**:
   - Reads secure configuration settings from a `.env` file using the `python-dotenv` package.

## Prerequisites

Make sure you have Python installed. You'll also need to install the project dependencies:

```bash
pip install Flask python-dotenv
```

## How to Run

1. Clone or download the repository.
2. Ensure the `.env` file is present in the root directory and contains the `secret_code` variable.
3. Run the application from your terminal:

```bash
python app.py
```

4. The server will start in debug mode. Open your web browser and go to:
   `http://127.0.0.1:5000/`

## Routes Info

- **`GET /`**: Renders the login page (`index.html`).
- **`POST /submit`**: Processes the login form submission. If the credentials are correct, it sets a session variable and renders the welcome page. If incorrect, it displays an error message.
- **`GET /logout`**: Clears the user's session data and redirects back to the login page.


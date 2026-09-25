# mEthics - Learning Flask Project

This is a web application built with [Flask](https://flask.palletsprojects.com/) to demonstrate core web development concepts like routing, template rendering (Jinja2), handling form submissions (GET & POST), session management, and user authentication & registration flows.

<p align="center">
  <img src="sc.png" width="700" alt="Login Page Screenshot">
</p>


## Recent Changes & Updates

### 1. Last Commit (`785c618`)
- **Added Account Creation & Error Templates**:
  - `templates/create-account.html`: Modern user registration page with animated floating background elements.
  - `templates/error.html`: Custom error page shown when user authentication fails.
- **Cleanup**:
  - Removed outdated `templates/admin.html` dashboard in favor of the dynamic `user.html` dashboard.

### 2. Recent Updates (Authentication & Account Creation)
- **Account Creation Logic (`app.py`)**:
  - Added `GET /render_create_account`: Renders the account registration view (`create-account.html`).
  - Added `POST /create_account`: Handles new user signups.
    - Validates that `password` and `confirm_password` match.
    - Checks for existing usernames and renders `username_already_exist.html` if the username is taken.
    - Stores the new user, establishes a user session (`session['user']`), and renders `user.html`.
- **Improved Login Flow**:
  - `POST /submit`: Updated invalid credentials handling to render the custom `error.html` page instead of raw text. Successful logins render `user.html` with personalized user greetings.
- **New Template**:
  - `templates/username_already_exist.html`: A friendly error screen alerting the user that the chosen username is already registered, with a "Try again" button linking back to `/render_create_account`.
- **UI & Form Enhancements**:
  - `templates/create-account.html`: Configured form submission (`POST /create_account`) and submit triggers.
  - `templates/error.html`: Styled with "No Account found !" messaging and quick navigation buttons ("Create account" and "Try again").
  - `templates/login.html`: Polished card styling (transparent background, softened shadows, refined input padding, and label typography).

---

## Project Structure

- **`app.py`**: The main entry point for the Flask application. Contains server setup, routing logic, session management, and authentication/registration handlers.
- **`templates/`**: Directory containing HTML templates rendered using Jinja2:
  - **`index.html`**: Landing page with navigation and responsive hero section.
  - **`login.html`**: User login form.
  - **`create-account.html`**: User registration form with password confirmation.
  - **`user.html`**: Authenticated user dashboard displaying greeting and logout button.
  - **`error.html`**: Error page displayed when login credentials do not match any account.
  - **`username_already_exist.html`**: Error page displayed when an account creation username is already in use.
- **`.env`**: Stores environment variables (such as Flask's `secret_code`).
- **`requirements.txt`**: Lists Python dependencies (`Flask`, `python-dotenv`, `gunicorn`).
- **`flask.txt`**: Learning notes on Flask routing, HTTP methods, and Jinja2 templating.
- **`rivision.py`**: Experimental and revision script for Flask concepts.

---

## Features

1. **User Authentication & Login**:
   - Validates user credentials submitted via `POST /submit`.
   - Grants session access upon valid login; presents dedicated error page (`error.html`) upon failure.
2. **Account Creation & Validation**:
   - Form submission handling with password verification (`password == confirm_password`).
   - Duplicate username detection rendering `username_already_exist.html`.
   - Automatic session creation upon successful registration.
3. **Session Management**:
   - Utilizes Flask sessions (`session['username']`, `session['user']`) to manage login state.
   - Secure logout route (`GET /logout`) that clears session data and redirects to the home page.
4. **Animated & Responsive UI**:
   - Clean, modern layout with dynamic floating SVG icon animations.
   - Dedicated feedback pages with intuitive navigation links.
5. **Environment Configuration**:
   - Loads sensitive configuration like `secret_code` via `python-dotenv`.

---
## Prerequisites

Make sure you have Python installed. Install the project dependencies using `requirements.txt`:

```bash
pip install -r requirements.txt
```
Ensure a `.env` file exists in the root directory with your secret key:

```env
secret_code=your_secret_key_here
```

---
## How to Run

1. Clone or download the repository.
2. Run the application from your terminal:

```bash
python app.py
```
3. The server starts in debug mode by default. Open your browser and navigate to:

*Note: For production deployments, `gunicorn` is available. Run `gunicorn app:app`.*

---

## Routes Info

| Route | Method | Description |
| :--- | :--- | :--- |
| `/` | `GET` | Renders the main landing page (`index.html`). |
| `/login` | `GET` | Displays the login form (`login.html`). |
| `/submit` | `POST` | Authenticates login credentials. Renders `user.html` on success, or `error.html` on invalid credentials. |
| `/render_create_account` | `GET` | Displays the account creation page (`create-account.html`). |
| `/create_account` | `POST` | Processes registration. Validates password confirmation and duplicate usernames (`username_already_exist.html`). Creates user session on success. |
| `/logout` | `GET` | Clears active session and redirects to the landing page (`/`). |

---

## Activated server will look like this :-

<p align="center">
  <img src="sc2.png" alt="Login Page Screenshot">
</p>
<br>

## Note -
### --> **Frontend and UI design of website is designed by AI** because this project focuses on backend, so backend is completely written by Author (Mohit singh)
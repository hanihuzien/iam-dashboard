# IAM Access Management Dashboard

## Project Overview
The IAM Access Management Dashboard is a simple web application built with Python, Flask, and SQLite. It demonstrates basic identity and access management tasks by allowing users to manage accounts and review recent account activity.

## Features
- View total, active, and inactive user counts
- Add user accounts
- Edit user names, email addresses, and roles
- Deactivate user accounts
- Prevent duplicate email addresses
- Record account-management actions in an audit log

## Technologies Used
- Python
- Flask
- SQLite
- HTML

## Requirements
- Python 3
- pip (Python package installer)

## Setup and Run Instructions

1. Download or clone this repository.
2. Open a terminal in the project folder.
3. Install the required package:

   `python3 -m pip install -r requirements.txt`

4. Start the application:

   `python3 app.py`

5. Open your browser and visit:

   `http://127.0.0.1:5000`

The application initializes its SQLite database and creates sample users when the database does not already contain users.

## Project Structure

- `app.py` — Flask application and database operations
- `templates/index.html` — Main dashboard
- `templates/edit_user.html` — User editing page
- `requirements.txt` — Python dependency list
- `.gitignore` — Files excluded from Git tracking

## Notes
This project is an educational prototype and is not intended for production use. It does not implement authentication or production-grade security controls.

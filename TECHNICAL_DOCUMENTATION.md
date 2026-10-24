# Technical Documentation — IAM Access Management Dashboard

## 1. System Overview
The IAM Access Management Dashboard is a web application developed to demonstrate basic identity and access management operations. It uses Python and Flask for application logic, HTML templates for the user interface, and SQLite for data storage.

## 2. System Architecture
The application follows a simple web application architecture:

- **Presentation layer:** HTML templates rendered by Flask.
- **Application layer:** Flask routes process user requests and perform account-management operations.
- **Data layer:** SQLite stores user account information and audit log entries.

## 3. Technologies
- Python 3
- Flask
- SQLite
- HTML
- Jinja2 templating through Flask

## 4. Database Design

### Users table
| Field | Type | Description |
|---|---|---|
| id | INTEGER | Unique user identifier; primary key |
| name | TEXT | User's name |
| email | TEXT | User's email address; must be unique |
| role | TEXT | User's assigned role label |
| active | INTEGER | Account status: 1 for active, 0 for inactive |

### Audit Logs table
| Field | Type | Description |
|---|---|---|
| id | INTEGER | Unique audit entry identifier; primary key |
| action | TEXT | Type of action performed |
| details | TEXT | Description of the action |
| timestamp | TEXT | Date and time recorded for the action |

## 5. Main Application Routes
| Route | Method | Purpose |
|---|---|---|
| `/` | GET | Displays the dashboard, user accounts, statistics, and recent audit activity |
| `/add_user` | POST | Validates and adds a user account |
| `/edit_user/<user_id>` | GET, POST | Displays the editing form and saves user changes |
| `/deactivate_user/<user_id>` | POST | Marks a user account as inactive |

## 6. Application Logic
- The database initialization function creates the required tables if they do not exist.
- Sample accounts are inserted when the users table is empty.
- User input is checked for required fields.
- Email addresses are converted to lowercase, and SQLite's unique constraint prevents duplicate email addresses.
- Account-management actions are recorded in the audit log.
- Dashboard statistics are calculated from the stored user accounts.
- The dashboard displays the 10 most recent audit entries.

## 7. Installation and Execution
1. Install Python 3.
2. Install dependencies with `python3 -m pip install -r requirements.txt`.
3. Start the application with `python3 app.py`.
4. Visit `http://127.0.0.1:5000` in a browser.

## 8. Testing
The application was manually tested for:
- Dashboard loading and account statistics
- Adding a user
- Handling duplicate email addresses
- Editing a user
- Deactivating a user
- Recording and displaying audit log entries

## 9. Limitations and Future Improvements
This project is an educational prototype and is not production-ready. It does not implement authentication, authorization enforcement, or production-grade security protections.

Potential future improvements include:
- User authentication
- Enforced role-based access control
- More comprehensive input validation
- Automated tests
- Deployment to a hosted environment

## 10. AI Assistance
AI assistance was used to support development, explain implementation steps, help troubleshoot errors, and assist with project documentation. The application was run and manually tested during development.

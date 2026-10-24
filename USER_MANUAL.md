# User Manual — IAM Access Management Dashboard

## 1. Introduction
The IAM Access Management Dashboard is a web application for managing user accounts and reviewing account-management activity.

## 2. Starting the Application
1. Make sure Python 3 and Flask are installed.
2. Open a terminal in the project folder.
3. Run `python3 app.py`.
4. Open `http://127.0.0.1:5000` in your web browser.

## 3. Viewing the Dashboard
The dashboard displays the total number of user accounts, active accounts, and inactive accounts. The user table lists the available accounts and their roles.

## 4. Adding a User
1. Locate the add-user form on the dashboard.
2. Enter the user's name, email address, and role.
3. Submit the form.
4. A success message appears if the user is added. An existing email address cannot be reused.

New accounts are created as active accounts.

## 5. Editing a User
1. Find the account in the user table.
2. Click its **Edit** link.
3. Update the name, email address, or role.
4. Submit the changes.

The dashboard displays a message indicating whether the update succeeded.

## 6. Deactivating a User
1. Find the account in the user table.
2. Click its **Deactivate** button.
3. Return to the dashboard and confirm that the account is now inactive.

Deactivation changes the account's status; it does not delete the account.

## 7. Reviewing the Audit Log
Scroll to the **Audit Log** section to review recent user-management actions. Entries include the action, details, and date and time. The dashboard displays up to the 10 most recent entries.

## 8. Troubleshooting
- **The page will not open:** Confirm the Flask application is running in the terminal, then refresh the browser.
- **The email is already in use:** Enter a different email address.
- **The application will not start:** Check that Python 3 and Flask are installed and that the terminal is in the project folder.

## 9. Important Notes
This is an educational prototype. It is not designed for production use and does not include user login or production-grade security controls.


from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3
from datetime import datetime
app = Flask(__name__)
app.secret_key = "iam-dashboard-dev-key-change-me"

DATABASE = "iam.db"


def get_db_connection():
    connection = sqlite3.connect(DATABASE)
    connection.row_factory = sqlite3.Row
    return connection
def log_action(action, details):
    connection = get_db_connection()

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    connection.execute(
        """
        INSERT INTO audit_logs (action, details, timestamp)
        VALUES (?, ?, ?)
        """,
        (action, details, timestamp)
    )

    connection.commit()
    connection.close()

def initialize_database():
    connection = get_db_connection()

    connection.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            role TEXT NOT NULL,
            active INTEGER NOT NULL DEFAULT 1
        )
    """)
    
    connection.execute("""
        CREATE TABLE IF NOT EXISTS audit_logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            action TEXT NOT NULL,
            details TEXT NOT NULL,
            timestamp TEXT NOT NULL
        )
    """)

    user_count = connection.execute(
        "SELECT COUNT(*) FROM users"
    ).fetchone()[0]

    if user_count == 0:
        sample_users = [
            ("Alex Morgan", "alex@example.com", "Administrator", 1),
            ("Jordan Lee", "jordan@example.com", "Manager", 1),
            ("Sam Taylor", "sam@example.com", "Employee", 1),
            ("Casey Smith", "casey@example.com", "Auditor", 0),
        ]

        connection.executemany("""
            INSERT INTO users (name, email, role, active)
            VALUES (?, ?, ?, ?)
        """, sample_users)

    connection.commit()
    connection.close()


@app.route("/")
def dashboard():
    connection = get_db_connection()

    users = connection.execute(
        "SELECT * FROM users ORDER BY id"
    ).fetchall()
    logs = connection.execute(
        "SELECT * FROM audit_logs ORDER BY id DESC LIMIT 10"
    ).fetchall()
    total_users = len(users)
    active_users = sum(user["active"] for user in users)
    inactive_users = total_users - active_users

    connection.close()

    return render_template(
        "index.html",
        users=users,
        total_users=total_users,
        active_users=active_users,
        inactive_users=inactive_users,
        logs=logs
    )

@app.route("/add_user", methods=["POST"])
def add_user():
    name = request.form.get("name", "").strip()
    email = request.form.get("email", "").strip().lower()
    role = request.form.get("role", "").strip()

    if not name or not email or not role:
        flash("Please fill in all fields.")
        return redirect(url_for("dashboard"))

    connection = get_db_connection()

    try:
        connection.execute(
            """
            INSERT INTO users (name, email, role, active)
            VALUES (?, ?, ?, 1)
            """,
            (name, email, role)
        )
        connection.commit()
        log_action("User Added", f"Added user: {name} ({email}), Role: {role}")
        flash("User added successfully!")

    except sqlite3.IntegrityError:
        flash("That email address already exists.")

    finally:
        connection.close()

    return redirect(url_for("dashboard"))

@app.route("/deactivate_user/<int:user_id>", methods=["POST"])
def deactivate_user(user_id):
    connection = get_db_connection()

    user = connection.execute(
        "SELECT name FROM users WHERE id = ?",
        (user_id,)
    ).fetchone()

    connection.execute(
        "UPDATE users SET active = 0 WHERE id = ?",
        (user_id,)
    )

    connection.commit()
    connection.close()

    if user:
        log_action(
            "User Deactivated",
            f"Deactivated account for: {user['name']} (User ID: {user_id})"
        )

    flash("User deactivated successfully.")
    return redirect(url_for("dashboard"))


@app.route("/edit_user/<int:user_id>", methods=["GET", "POST"])
def edit_user(user_id):
    connection = get_db_connection()

    user = connection.execute(
        "SELECT * FROM users WHERE id = ?",
        (user_id,)
    ).fetchone()

    if user is None:
        connection.close()
        flash("User not found.")
        return redirect(url_for("dashboard"))

    if request.method == "POST":
        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip().lower()
        role = request.form.get("role", "").strip()

        if not name or not email or not role:
            flash("Please fill in all fields.")
            connection.close()
            return redirect(url_for("edit_user", user_id=user_id))

        try:
            connection.execute(
                """
                UPDATE users
                SET name = ?, email = ?, role = ?
                WHERE id = ?
                """,
                (name, email, role, user_id)
            )
            connection.commit()
            log_action(
                "User Edited",
                f"Updated information for user: {name} (User ID: {user_id})"
            )
            flash("User updated successfully!")

        except sqlite3.IntegrityError:
            flash("That email address is already in use.")

        finally:
            connection.close()

        return redirect(url_for("dashboard"))

    connection.close()
    return render_template("edit_user.html", user=user)

if __name__ == "__main__":
    initialize_database()
    app.run(debug=True)


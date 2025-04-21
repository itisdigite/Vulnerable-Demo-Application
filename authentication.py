from flask import Flask, render_template, request, redirect, url_for, flash, session
import sqlite3
import re
import hashlib
from flask import jsonify


app = Flask(__name__)
app.secret_key = 'secure_key'
PORT = 6005

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Login route
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
        user = cursor.fetchone()
        conn.close()

# Vulnerable code displaying specific error message
        if not user:
            flash("Invalid username")  # Vulnerable: Reveals if the username is incorrect
        elif user[2] != password:
            flash("Invalid password")  # Vulnerable: Reveals if the password is incorrect
        else:
            session['username'] = user[1]
            session['role'] = user[3]
            return redirect(url_for('dashboard'))

    # return render_template('auth_login.html')
# SECURE CODE: Uncomment the following to fix vulnerabilities 
        # if not user or user[2] != password:
        #     flash("Invalid login credentials")  # Secure: Generic error message
        # else:
        #     session['username'] = user[1]
        #     session['role'] = user[3]
        #     return redirect(url_for('dashboard'))

    return render_template('auth_login.html')


# Dashboard route
@app.route('/dashboard')
def dashboard():
    if 'username' not in session:
        return redirect(url_for('login'))
    # return f"Welcome, {session['username']}! This is your dashboard."
    return render_template('auth_dashboard.html')

# Password reset route
@app.route('/password_reset', methods=['GET', 'POST'])
def password_reset():
    if request.method == 'POST':
        username = request.form.get('username')
        new_password = request.form.get('new_password')

        # VULNERABLE CODE: Allow password reuse
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute("SELECT password FROM users WHERE username = ?", (username,))
        user = cursor.fetchone()

        if not user:
            flash("Invalid username")
        else:
            # Uncomment the following secure code to prevent password reuse
            # SECURE CODE: Prevent password reuse
            # if user[0] == hash_password(new_password):  # Check if the new password is the same as the old one
            #     flash("Password cannot be reused")  # Secure: Prevent password reuse
            # else:
            #     cursor.execute("UPDATE users SET password = ? WHERE username = ?", 
            #                (hash_password(new_password), username))
                conn.commit()
                flash("Password reset successful")
        conn.close()

    return render_template('password_reset.html')

# @app.route('/confidential', methods=['GET', 'POST'])
@app.route('/confidential')
def confidential():
    if 'username' not in session:
        return redirect(url_for('login'))  # Redirect to login if the user is not logged in
    return render_template('confidential.html')  # Render the confidential.html page

# Verify password for Confidential File
@app.route('/verify_password', methods=['POST'])
def verify_password():
    if 'username' not in session:
        return jsonify(success=False), 403

    data = request.get_json()
    password = data.get('password')

    # Validate the password against the database
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("SELECT password FROM users WHERE username = ?", (session['username'],))
    user = cursor.fetchone()
    conn.close()

    if user and user[0] == password:   #Compare passwords
        return jsonify(success=True)
    else:
        return jsonify(success=False)

 

if __name__ == '__main__':
    app.run(debug=True, port=PORT)
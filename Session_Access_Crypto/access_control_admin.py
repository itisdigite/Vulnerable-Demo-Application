from flask import Flask, render_template, request, redirect, url_for, session, flash
import sqlite3
import json

app = Flask(__name__)
app.secret_key = 'admin_secret'
PORT = 5701

with open('common/users.json') as f:
    users = json.load(f)

# Login route for admins
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        # Check credentials in the database
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username = ? AND password = ? AND role = ?", 
                       (username, password, 'admin'))
        admin = cursor.fetchone()
        conn.close()

        if admin:
            session['username'] = admin[1]
            session['role'] = admin[3]
            return redirect(url_for('admin_dashboard'))
        else:
            flash('Invalid credentials')
    
    return render_template('login.html', portal='Admin')

# Admin dashboard route
@app.route('/admin_dashboard')
def admin_dashboard():
    if 'username' not in session or session.get('role') != 'admin':
        return redirect(url_for('login'))
    return render_template('admin_dashboard.html', admin=session.get('username'))

# Logout route
@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True, port=PORT)
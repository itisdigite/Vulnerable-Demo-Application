from flask import Flask, render_template, request, redirect, url_for, session, flash
import sqlite3
import json

app = Flask(__name__)
app.secret_key = 'user_secret'
PORT = 5700

with open('common/users.json') as f:
    users = json.load(f)


# Login route for users
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        # Check credentials in the database
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username = ? AND password = ? AND role = ?", 
                       (username, password, 'user'))
        user = cursor.fetchone()
        conn.close()

        if user:
            session['username'] = user[1]
            session['role'] = user[3]
            # return redirect(url_for('dashboard'))
            # VULNERABLE CODE: Pass role as a query parameter in the request
            return redirect(url_for('dashboard', role='user'))  # Role is passed in the URL

        else:
            flash('Invalid credentials')
    
    return render_template('login.html', portal='User')

# Dashboard route for users
@app.route('/dashboard')
def dashboard():
    #Vulnerable code starts here
    role = request.args.get('role', 'guest')  # Default to 'guest' if no role is provided
    if role == 'admin':
        return render_template('admin_dashboard.html', admin=session.get('username'))
    elif role == 'user':
        return render_template('dashboard.html', user=session.get('username'))
    else:
        return "Access Denied: Invalid Role", 403
    #Vulnerable code ends here

    # SECURE CODE: Uncomment the following to validate the role from the session instead of the query parameter
    # if 'username' not in session or session.get('role') != 'user':
    #     return "Access Denied: Invalid Role", 403
    # return render_template('dashboard.html', user=session.get('username'))

# Logout route
@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True, port=PORT)
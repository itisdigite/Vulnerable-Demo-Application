from flask import Flask, session, redirect, url_for, request, render_template, flash
import json

app = Flask(__name__)
app.secret_key = 'user_secret'
PORT = 5999

# Load users from JSON
with open('common/users.json') as f:
    users = json.load(f)

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        uname = request.form['username']
        pwd = request.form['password']

        # Validate only 'user' role logins here
        if uname in users and users[uname]['password'] == pwd and users[uname]['role'] == 'user':
            session['username'] = uname
            session['role'] = 'user'
            return redirect(url_for('dashboard'))
        flash("Invalid credentials")
    return render_template('login.html', portal='User')

@app.route('/dashboard')
def dashboard():
    # --- VULNERABLE BEHAVIOR ---
    if session.get('role') == 'admin':
        flash('⚠️ Admin session injected into user session! (VULNERABLE)')
        
        # --- SECURE CODE START ---
        # session.clear()
        # flash('❌ Tampered session detected. Logged out for safety.')
        # return redirect(url_for('login'))
        # # --- SECURE CODE END ---

    elif session.get('role') != 'user':
        return redirect(url_for('login'))

    return render_template('dashboard.html', user=session.get('username'))


if __name__ == '__main__':
    app.run(debug=True, port=PORT)

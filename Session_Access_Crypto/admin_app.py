from flask import Flask, session, redirect, url_for, request, render_template, flash
import json

app = Flask(__name__)
app.secret_key = 'user_secret'
PORT = 6001

with open('common/users.json') as f:
    users = json.load(f)

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        uname = request.form['username']
        pwd = request.form['password']
        if uname in users and users[uname]['password'] == pwd and users[uname]['role'] == 'admin':
            session['username'] = uname
            session['role'] = 'admin'
            return redirect(url_for('admin_dashboard'))
        flash("Invalid credentials")
    return render_template('login.html', portal='Admin')

@app.route('/admin_dashboard')
def admin_dashboard():
    if session.get('role') != 'admin':
        return redirect(url_for('login'))
    return render_template('admin_dashboard.html', admin=session.get('username'))


if __name__ == '__main__':
    app.run(debug=True, port=PORT)

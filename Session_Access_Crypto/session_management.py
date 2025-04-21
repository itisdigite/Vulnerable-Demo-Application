# from flask import Flask, request, redirect, session, url_for, render_template_string
# from flask_httpauth import HTTPBasicAuth
# import secrets
# import uuid

# # Flask apps
# user_app = Flask(__name__)
# admin_app = Flask(__name__)

# # Secret keys for sessions
# user_app.secret_key = secrets.token_hex(16)
# admin_app.secret_key = secrets.token_hex(16)

# auth_user = HTTPBasicAuth()
# auth_admin = HTTPBasicAuth()

# # Dummy user credentials
# users = {
#     "user": "userpass"
# }
# admins = {
#     "admin": "adminpass"
# }

# # HTML Template for dashboard
# dashboard_template = """
# <h1>Welcome {{ role }}</h1>
# <p>This is the {{ role }} dashboard</p>
# """

# # Basic Auth verification
# @auth_user.verify_password
# def verify_user(username, password):
#     return users.get(username) == password

# @auth_admin.verify_password
# def verify_admin(username, password):
#     return admins.get(username) == password

# # Function to mitigate session fixation by regenerating session ID
# # def regenerate_session():
# #     session.clear()  # Clear any existing session data
# #     session['sid'] = str(uuid.uuid4())  # Generate a new unique session ID

# # Admin Routes
# @admin_app.route('/')
# @auth_admin.login_required
# def admin_login():
#     # regenerate_session()  # Secure session regeneration
#     session['user'] = 'admin'
#     return redirect(url_for('admin_dashboard'))

# @admin_app.route('/dashboard')
# def admin_dashboard():
#     if session.get('user') == 'admin':
#         return render_template_string(dashboard_template, role='Admin')
#     return "Access Denied"

# # User Routes
# @user_app.route('/')
# @auth_user.login_required
# def user_login():
#     # regenerate_session()  # Secure session regeneration
#     session['user'] = 'user'
#     return redirect(url_for('user_dashboard'))

# @user_app.route('/dashboard')
# def user_dashboard():
#     if session.get('user') == 'user':
#         return render_template_string(dashboard_template, role='User')
#     elif session.get('user') == 'admin':
#         # Mitigated: session cannot be reused due to regeneration
#         # return "Access Denied"
#         return "Access Denied"

# if __name__ == '__main__':
#     from threading import Thread
#     Thread(target=lambda: admin_app.run(port=6001)).start()
#     Thread(target=lambda: user_app.run(port=5999)).start()

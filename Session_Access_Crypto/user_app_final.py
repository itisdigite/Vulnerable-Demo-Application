# from flask import Flask, request, redirect, session, url_for, render_template_string
# from flask_httpauth import HTTPBasicAuth
# import secrets
# import uuid

# user_app = Flask(__name__)
# user_app.secret_key = secrets.token_hex(16)

# auth_user = HTTPBasicAuth()

# users = {
#     "user": "userpass"
# }

# dashboard_template = """
# <h1>Welcome {{ role }}</h1>
# <p>This is the {{ role }} dashboard</p>
# """

# @auth_user.verify_password
# def verify_user(username, password):
#     return users.get(username) == password

# # def regenerate_session():
# #     session.clear()
# #     session['sid'] = str(uuid.uuid4())

# @user_app.route('/')
# @auth_user.login_required
# # def user_login():
# #     regenerate_session()
# #     session['user'] = 'user'
# #     return redirect(url_for('user_dashboard'))

# @user_app.route('/dashboard')
# def user_dashboard():
#     if session.get('user') == 'user':
#         return render_template_string(dashboard_template, role='User')
#     elif session.get('user') == 'admin':
#         return "This is admin dashboard"
#     return "Access Denied"

# if __name__ == '__main__':
#     user_app.run(port=5999)


# Admin app final code - 
# from flask import Flask, request, redirect, session, url_for, render_template_string
# from flask_httpauth import HTTPBasicAuth
# import secrets
# import uuid

# admin_app = Flask(__name__)
# admin_app.secret_key = secrets.token_hex(16)

# auth_admin = HTTPBasicAuth()

# admins = {
#     "admin": "adminpass"
# }

# dashboard_template = """
# <h1>Welcome {{ role }}</h1>
# <p>This is the {{ role }} dashboard</p>
# """

# @auth_admin.verify_password
# def verify_admin(username, password):
#     return admins.get(username) == password

# # def regenerate_session():
# #     session.clear()
# #     session['sid'] = str(uuid.uuid4())

# @admin_app.route('/')
# @auth_admin.login_required
# # def admin_login():
# #     regenerate_session()
# #     session['user'] = 'admin'
# #     return redirect(url_for('admin_dashboard'))

# @admin_app.route('/dashboard')
# def admin_dashboard():
#     if session.get('user') == 'admin':
#         return render_template_string(dashboard_template, role='Admin')
#     elif session.get('user') == 'user':
#         return "This is user dashboard"
#     return "Access Denied"

# if __name__ == '__main__':
#     admin_app.run(port=6001)
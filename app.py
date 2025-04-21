from flask import Flask, render_template, request, session, redirect, url_for
import sqlite3
import html
# from auth import auth

app = Flask(__name__)
app.secret_key = 'your-secret-key'  # In production, use a secure random key
# Register the auth blueprint
# app.register_blueprint(auth, url_prefix='/auth')

@app.route('/')
def home():
    return render_template('home.html')

# Input Validation Routes
@app.route('/input-validation')
def input_validation():
    return render_template('search.html')

@app.route('/input-validation/search', methods=['GET'])
def search_vulnerable():
    search_term = request.args.get('q', '')
    
    # VULNERABLE CODE - SQL Injection possible
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    # Uncomment below 2 lines to turn off vulnerable code
    # query = f"SELECT * FROM users WHERE username = '{search_term}'"
    # cursor.execute(query)
    # Uncomment below code for secure input validation
    query = "SELECT * FROM users WHERE username = ?"
    cursor.execute(query, (search_term,))
    results = cursor.fetchall()
    conn.close()
    return render_template('search_results.html', results=results)

#--------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------
# *********** Secure Code Snippet ***********************
# @app.route('/input-validation/search-secure', methods=['GET'])
# def search_secure():
#     search_term = request.args.get('q', '')
    
#     # SECURE CODE - Parameterized Query
#     conn = sqlite3.connect('database.db')
#     cursor = conn.cursor()
#     # query = "SELECT * FROM users WHERE username = ?"
#     # cursor.execute(query, (search_term,))
#     results = cursor.fetchall()
#     conn.close()
    
#     return render_template('search_results.html', results=results)

# ==============================================================================================================================
# ==============================================================================================================================
# Output Encoding
@app.route('/output-encoding')
def output_encoding():
    return render_template('comment_form.html')

@app.route('/output-encoding/comment', methods=['POST'])
def add_comment():
    comment = request.form.get('comment', '')
    
    # VULNERABLE CODE - No output encoding
    return f"<div>Your comment: {comment}</div>"

    # Uncomment below code for secure output encoding
    # safe_comment = html.escape(comment)
    # return f"<div>Your comment: {safe_comment}</div>"

#--------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------
# ***********Secure Code Snippet ***********************
# @app.route('/output-encoding/secure')
# def output_encoding():
#     return render_template('comment_form.html')

# @app.route('/output-encoding/comment-secure', methods=['GET', 'POST'])
# def add_comment_secure():
#     comment = request.form.get('comment', '')
    
#     # SECURE CODE - HTML escaping
#     safe_comment = html.escape(comment)
#     return f"<div>Your comment: {safe_comment}</div>"

# ==============================================================================================================================
# ==============================================================================================================================


# *********************** Vulnerable Authentication Implementation *********************************
# @app.route('/auth/signup', methods=['GET', 'POST'])
# def signup_vulnerable():
#     if request.method == 'POST':
#         username = request.form.get('username')
#         password = request.form.get('password')
        
#         # VULNERABLE CODE - No password validation, plain text storage
#         conn = sqlite3.connect('database.db')
#         cursor = conn.cursor()
#         cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", 
#                       (username, password))
#         conn.commit()
#         conn.close()
#         return redirect(url_for('login_vulnerable'))
    
#     return render_template('signup.html')

# @app.route('/auth/login', methods=['GET', 'POST'])
# def login_vulnerable():
#     if request.method == 'POST':
#         username = request.form.get('username')
#         password = request.form.get('password')
        
#         # VULNERABLE CODE - No password hashing, direct comparison
#         conn = sqlite3.connect('database.db')
#         cursor = conn.cursor()
#         cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", 
#                       (username, password))
#         user = cursor.fetchone()
#         conn.close()
        
#         if user:
#             return "Successful Login"
#         else:
#             return "Invalid login credentials"
    
#     return render_template('login.html')




























# ==============================================================================================================================
# ==============================================================================================================================
# # Secure Authentication Implementation
# import re
# import hashlib
# import secrets

# def validate_password(password):
#     # Password requirements:
#     # - Minimum 8 characters
#     # - At least 1 special character
#     # - At least 1 uppercase letter
#     # - At least 1 lowercase letter
#     # - At least 1 digit
#     pattern = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'
#     return bool(re.match(pattern, password))

# def hash_password(password):
#     # Generate a random salt
#     salt = secrets.token_hex(16)
#     # Hash the password with the salt
#     hashed = hashlib.sha256((password + salt).encode()).hexdigest()
#     return f"{salt}:{hashed}"

# def verify_password(stored_password, provided_password):
#     salt, hashed = stored_password.split(':')
#     return hashlib.sha256((provided_password + salt).encode()).hexdigest() == hashed

# @app.route('/auth/signup-secure', methods=['GET', 'POST'])
# def signup_secure():
#     if request.method == 'POST':
#         username = request.form.get('username')
#         password = request.form.get('password')
        
#         # SECURE CODE - Password validation and hashing
#         if not validate_password(password):
#             return "Password does not meet requirements", 400
        
#         hashed_password = hash_password(password)
        
#         conn = sqlite3.connect('database.db')
#         cursor = conn.cursor()
#         try:
#             cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", 
#                          (username, hashed_password))
#             conn.commit()
#             return redirect(url_for('login_secure'))
#         except sqlite3.IntegrityError:
#             return "Username already exists", 400
#         finally:
#             conn.close()
    
#     return render_template('signup.html')

# @app.route('/auth/login-secure', methods=['GET', 'POST'])
# def login_secure():
#     if request.method == 'POST':
#         username = request.form.get('username')
#         password = request.form.get('password')
        
#         # SECURE CODE - Password verification with hashing
#         conn = sqlite3.connect('database.db')
#         cursor = conn.cursor()
#         cursor.execute("SELECT password FROM users WHERE username = ?", (username,))
#         result = cursor.fetchone()
#         conn.close()
        
#         if result and verify_password(result[0], password):
#             return "Successful Login"
#         else:
#             return "Invalid login credentials"
    
#     return render_template('login.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)


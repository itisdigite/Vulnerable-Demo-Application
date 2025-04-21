from flask import Flask
from access_control import access_bp, init_db

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'  # Change this to a secure secret key

# Register blueprints
app.register_blueprint(access_bp)

# Initialize database
init_db()

if __name__ == '__main__':
    app.run(debug=True, port=5700)
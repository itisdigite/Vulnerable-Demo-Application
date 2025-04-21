from flask import Flask, request, render_template_string
import hashlib
import bcrypt
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env


# Setup Flask app
app = Flask(__name__)

# Template for UI
template = """
<!doctype html>
<html>
<head>
  <title>Cryptographic Practices Demo</title>
</head>
<body style="font-family:sans-serif; background:#f4f4f4; padding:20px;">
  <h2>🔐 Cryptographic Practices Demo</h2>

  <form method="POST">
    <label>Enter password:</label><br>
    <input type="text" name="password" required><br><br>
    <button name="method" value="vulnerable">Vulnerable Hash (MD5 + Hardcoded Key)</button>
    <button name="method" value="secure">Secure Hash (bcrypt + Env Key)</button>
  </form>

  {% if result %}
    <div style="margin-top:20px; padding:15px; background:white; border:1px solid #ccc;">
      <h4>Method Used: {{ method }}</h4>
      <p><strong>Key Used:</strong> {{ key }}</p>
      <p><strong>Hashed Output:</strong><br>{{ result }}</p>
    </div>
  {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    key_used = ""
    method = ""

    if request.method == "POST":
        password = request.form["password"]
        method = request.form["method"]

        if method == "vulnerable":
            # 🔓 VULNERABLE: Hardcoded key and insecure MD5 hash
            key_used = "HARDCODED_KEY_123"
            combined = password + key_used
            result = hashlib.md5(combined.encode()).hexdigest()

        elif method == "secure":
            # ✅ SECURE: Key from env + bcrypt hashing
            # key_used = os.getenv("SECURE_KEY", "ENV_KEY_NOT_SET")
            # combined = password + key_used
            result = bcrypt.hashpw(combined.encode(), bcrypt.gensalt()).decode()

    return render_template_string(template, result=result, key=key_used, method=method.capitalize() if method else "")

if __name__ == "__main__":
    # Set secure key in environment for demo purpose
    os.environ["SECURE_KEY"] = "ENV_KEY_456"
    app.run(debug=True, port=5002)

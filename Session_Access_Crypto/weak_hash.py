from flask import Flask, request, render_template_string
import hashlib
# import bcrypt  # Uncomment to use bcrypt

app = Flask(__name__)

HTML = '''
<!doctype html>
<title>Password Hashing Demo</title>
<h2>🔐 Password Hashing Demonstration</h2>
<form method="post">
  Enter Password: <input type="password" name="password" required>
  <input type="submit" value="Generate Hash">
</form>
{% if hash_result %}
  <p><strong>Generated Hash:</strong> {{ hash_result }}</p>
{% endif %}
'''

# Insecure MD5 hash function
def hash_with_md5(password):
    return hashlib.md5(password.encode()).hexdigest()

# Secure bcrypt hash function (Commented)
# def hash_with_bcrypt(password):
#     return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

@app.route('/', methods=['GET', 'POST'])
def hash_password():
    hash_result = None
    if request.method == 'POST':
        password = request.form['password']
        
        # Use MD5 (Insecure)
        hash_result = hash_with_md5(password)
        
        # Use bcrypt (Secure)
        # hash_result = hash_with_bcrypt(password)

    return render_template_string(HTML, hash_result=hash_result)


if __name__ == '__main__':
    app.run(debug=True, port=5002)

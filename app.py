from flask import Flask, render_template, request
import random
import string

app = Flask(__name__)

def generate_password(length, use_upper, use_lower, use_digits, use_symbols):
    options = [
        use_upper and string.ascii_uppercase,
        use_lower and string.ascii_lowercase,
        use_digits and string.digits,
        use_symbols and string.punctuation
    ]
    characters = ''.join(filter(None, options))
    if not characters:
        return "Error: No character types selected."
    return ''.join(random.choice(characters) for _ in range(length))

@app.route('/', methods=['GET', 'POST'])
def index():
    password = ''
    if request.method == 'POST':
        try:
            length = int(request.form['length'])
            use_upper = 'upper' in request.form
            use_lower = 'lower' in request.form
            use_digits = 'digits' in request.form
            use_symbols = 'symbols' in request.form
            password = generate_password(length, use_upper, use_lower, use_digits, use_symbols)
        except ValueError:
            password = 'Please enter a valid number.'
    return render_template('password.html', password=password)

if __name__ == '__main__':
    app.run(debug=True)

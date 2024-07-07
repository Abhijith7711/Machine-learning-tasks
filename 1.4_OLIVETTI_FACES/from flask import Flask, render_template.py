pip install Flask
from flask import Flask, render_template, request
app = Flask(__name__)

def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        number = int(request.form['number'])
        result = is_prime(number)
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)

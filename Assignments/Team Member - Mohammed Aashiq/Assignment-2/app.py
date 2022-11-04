from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/signin')
def signIn():
    return render_template('signIn.html')

@app.route('/sign up')
def signUp():
    return render_template('signUp.html')

@app.route('/about')
def about():
    return render_template('about.html')




if __name__ == '__main__':
    app.run(debug=True)
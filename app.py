from flask import Flask, render_template, request
app = Flask(__name__)
@app.route('/')
def home():
    return '<h1>Hello, World!</h1>' \
    '<h2>Welcome to my Flask app.</h2>' \
           
if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, redirect, url_for, render_template, request
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

if __name__ == "__main__":
    app.run()
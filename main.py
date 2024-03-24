from flask import Flask, render_template
import random

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/flowers')
def flowers():
    fw = open('flowers.txt', 'r')
    flowers = fw.read().split('\n')
    fw.close()
    return render_template('flowers.html',  flowers=flowers)


@app.route('/about_us')
def about_us():
    return render_template('about.html')


@app.route('/orders')
def orders():
    return render_template('orders.html')


if __name__ == "__main__":
    app.run(debug=True)

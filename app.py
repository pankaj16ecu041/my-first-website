from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # Flask looks into the /templates folder by default
    return render_template('index.html')

if __name__ == '__main__':
    # '0.0.0.0' allows the app to be accessible outside the container
    app.run(host='0.0.0.0', port=5000)

from flask import Flask, render_template, request, send_file, send_from_directory

app = Flask(__name__)


@app.route('/', methods=['GET'])
def homepage():
    return render_template('index.html')

@app.route('/canny', methods=['POST'])
def canny():
    return render_template('index.html')

@app.route('/sobel', methods=['POST'])
def sobel():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(port=3000, debug=True)
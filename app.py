from flask import Flask, render_template, request, send_file, send_from_directory

app = Flask(__name__)


@app.route('/', methods=['GET'])
def homepage():
     return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
     # -- uploaded file setup
     file = request.files['fileInput']
     file_path = "./uploads/img/" + file.filename
     file.save(file_path)

     # -- compression setup
     # get_name = file.filename.split(".")[0]
     # compression(file_path, get_name)

     return render_template('index.html')

@app.route('/test', methods=['GET'])
def sobel():
     return {
         'A' : 'AAA',
         'B' : 'BBB',
     }


if __name__ == '__main__':
     app.run(port=3000, debug=True)
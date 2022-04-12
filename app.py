from flask import Flask, render_template, request, send_file, send_from_directory
import cv2 as cv;
import io;

app = Flask(__name__, static_url_path = "/uploads", static_folder = "uploads")

@app.route('/', methods=['GET'])
def homepage():
     return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
     # -- uploaded file setup
     file = request.files.get('fileInput')
     file_path = "./uploads/img/" + file.filename
     file.save(file_path)

     # Canny edge detection --------------------------------------
     img = cv.imread(file_path, 0)
     edges = cv.Canny(img,100,200)

     cv.imwrite("./uploads/canny/" + file.filename, edges)

     # Sobel edge detection --------------------------------------
     img2 = cv.imread(file_path, 1)
     src = cv.GaussianBlur(img2, (3, 3), 0)
     grays = cv.cvtColor(src, cv.COLOR_BGR2GRAY)

     sobelx = cv.Sobel(grays, cv.CV_64F, dx=1, dy=0, ksize=3) # on X axis
     sobely = cv.Sobel(grays, cv.CV_64F, dx=0, dy=1, ksize=3) # on Y axis

     abs_grad_x = cv.convertScaleAbs(sobelx)
     abs_grad_y = cv.convertScaleAbs(sobely)

     grad = cv.addWeighted(abs_grad_x, 0.5, abs_grad_y, 0.5, 0)

     cv.imwrite("./uploads/sobel/" + file.filename, grad)

     return {
          "sobel" : "./uploads/sobel/" + file.filename,
          "canny" : "./uploads/canny/" + file.filename
     }

@app.route('/test', methods=['GET'])
def sobel():
     return {
         'A' : 'AAA',
         'B' : 'BBB',
     }


if __name__ == '__main__':
     app.run(port=3000, debug=True)
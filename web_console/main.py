from flask import Flask, send_from_directory
import cv2, base64, os

app = Flask(__name__)


cam = cv2.VideoCapture(0)


def encode(img):
    base64_start = "data:image/jpg;base64,"
    
    temp_image_name = 'temp.jpg'
    cv2.imwrite(temp_image_name,img)

    # Reopen image and encode in base64
    image = open(temp_image_name, 'rb') #open binary file in read mode
    image_read = image.read()
    image_64_encode = base64.encodestring(image_read)
    os.remove(temp_image_name)
    
    image_64_encode = base64_start + image_64_encode
    
    return image_64_encode

#BEGIN WEB SERVER #####################################################
@app.route('/index.html')
@app.route('/')
def index_html():
    return send_from_directory('web','index.html')

@app.route('/index.js')
def index_js():
    return send_from_directory('web','index.js')

@app.route('/index.css')
def index_css():
    return send_from_directory('web','index.css')
    
@app.route('/servo/<servo>/<degrees>')
def servo(servo,degrees):
    return servo + ' ' + degrees
    
@app.route('/image')
def image():
    global cam
    
    ret, frame = cam.read()
    
    
    
    return encode(frame)
    
#END WEB SERVER #######################################################

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, threaded=True)

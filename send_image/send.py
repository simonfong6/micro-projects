import cv2, base64, requests, os

FONT = cv2.FONT_HERSHEY_SIMPLEX

def request_from_server(img):
    URL = "http://face.mothakes.com/predict"
    temp_image_name = 'temp.jpg'
    cv2.imwrite(temp_image_name,img)

    # Reopen image and encode in base64
    image = open(temp_image_name, 'rb') #open binary file in read mode
    image_read = image.read()
    image_64_encode = base64.encodestring(image_read)
    os.remove(temp_image_name)
     
    # Defining a params dict for the parameters to be sent to the API
    PARAMS = {'file':image_64_encode}
    print(image_64_encode)
     
    # Dending get request and saving the response as response object
    r = requests.get(url = URL, params = PARAMS)
     
    # Print response
    data = r.json()

    return data

cam = cv2.VideoCapture(0)

def video():
    while(cam.isOpened()):
        ret,frame = cam.read()
        r = request_from_server(frame)
        name = r['label']
        cv2.putText(frame, name, (10, 30), FONT, 1, (0, 255, 0), 2)
        cv2.imshow("Person",frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
            
def snap():
    ret,frame = cam.read()
    r = request_from_server(frame)
    name_confidence = r['label'] + ' ' +  str(round(r['confidence'],2))
    cv2.putText(frame, name_confidence, (10, 30), FONT, 1, (0, 255, 0), 2)
    cv2.imshow("Prediction",frame)
    cv2.waitKey()

snap()



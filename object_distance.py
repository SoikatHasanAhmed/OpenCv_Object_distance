import time
import urllib.request
from methods import *
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--webcam', type=bool, default=True)
parser.add_argument('--url', type=str, default='http://192.168.0.4:8080/shot.jpg')

args = parser.parse_args()
#here we put the object 30 cm from the camera to calibraing
KNOWN_DISTANCE = 30.0

#the width of the object  in cm
KNOWN_WIDTH = 3.0
#we use a ip webcam for capture video

url = args.url
print("<<<---- taking calibrating Image ---->>>")
time.sleep(2)
if args.webcam:
    cap =  cv2.VideoCapture(0)
    _,c_image = cap.read()


else:
    imgResp = urllib.request.urlopen(url)
    imgNp = np.array(bytearray(imgResp.read()), dtype=np.uint8)
    c_image = cv2.imdecode(imgNp, -1)



marker = find_marker(c_image)
focalLength = (marker[1][0] * KNOWN_DISTANCE) / KNOWN_WIDTH


time.sleep(2)

print("<<<---- Main program Staring ---->>>")

while True:
    if args.webcam:
        _,image = cap.read()
    else:
        imgResp = urllib.request.urlopen(url)
        image = np.array(bytearray(imgResp.read()), dtype=np.uint8)
    # image = cv2.imdecode(imgNp, -1)



    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    marker = find_marker(image)
    CM = distance_to_camera(KNOWN_WIDTH, focalLength, marker[1][0])

    #print the output
    cv2.putText(image, "%.2fcm" % CM,
                (image.shape[1] - 350, image.shape[0] - 15), cv2.FONT_HERSHEY_SIMPLEX,
                2.0, (255, 0, 0), 3)
    cv2.imshow("image", image)
    key = cv2.waitKey(1)
    #Press Esc to stop the program
    if key == 27:
        break


cv2.destroyAllWindows()

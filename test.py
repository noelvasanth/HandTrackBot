import cv2
from picamera import PiCamera
import numpy as np
#from sklearn.metrics import pairwise
from picamera.array import PiRGBArray
import time
from utils import detector_utils as detector_utils
from PCA9685 import PCA9685 as Robot

#import handtracking graph
detection_graph, sess = detector_utils.load_inference_graph()
num_hands_detect = 1

#initialize robot arm
pwm = Robot(0x40, debug=False)
pwm.setPWMFreq(50)
pwm_0 = 1500
pwm_1 = 1750
pwm_2 = 1000
pwm.setServoPulse(0,pwm_0) # initialize the 0th pwm
pwm.setServoPulse(1,pwm_1) # Setting the arm upright
pwm.setServoPulse(2,pwm_2) # Look down
pwm_0_factor, pwm_2_factor = 3, 2

# initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 5
rawCapture = PiRGBArray(camera, size=(640, 480))
cam_center = np.array([160, 120])

# allow the camera to warmup
time.sleep(0.1)

# hand tracking parameters
score_treshold = 0.2
resize = (320,240)
hand_confidence_score = 0.5

for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    print("frame")
    # Capture and resize frame    
    frame = frame.array
    flipped = cv2.flip(frame, -1)
    flipped = cv2.cvtColor(flipped, cv2.COLOR_BGR2RGB)
    flipped = cv2.resize(flipped, resize)
    # Get hand detection object
    boxes, scores = detector_utils.detect_objects(flipped, detection_graph, sess)
   
    #only continue if confidence score is met
    if scores[0] > hand_confidence_score:
	    detector_utils.draw_box_on_image(num_hands_detect, score_treshold, scores, boxes, flipped.shape[0], flipped.shape[1], flipped)
	    top, left, bottom, right = boxes[0][0]*flipped.shape[1], boxes[0][1]*flipped.shape[0], boxes[0][2]*flipped.shape[1], boxes[0][3]*flipped.shape[0]
	   
	    #get coordinates and calculate center
	    x = np.array([left, right], dtype = np.int)
	    y = np.array([top, bottom], dtype = np.int)
	    hand_center = int((max(x)+min(x))/2), int((max(y)+min(y))/2)
	    
	    # draw center of hand on image
	    flipped = cv2.circle(flipped, hand_center, 5, (255,0,0), 2)
	    
	    #convert hand_center to nparray
	    hand_center = np.array([hand_center[0],hand_center[1]])
	    
	    #calculate the distance to the center in pixels
	    distance_to_center = cam_center - hand_center
	    
	    
	    pwm_0 = pwm_0 + distance_to_center[0]*pwm_0_factor
	    if pwm_0 > 2500:
	         pwm_0 = 2500
	    if pwm_0 < 500:
	         pwm_0 = 500 
	    pwm_2 = int(pwm_2 + distance_to_center[1]*pwm_2_factor)
	    if pwm_2 > 2500:
	         pwm_2 = 2500
	    if pwm_2 < 800:
	         pwm_2 = 800
	    
	    print((pwm_0, pwm_2), distance_to_center)
	 
    
    
    #pwm_0, x_condt = 1500, float(hand_center[0]/640.0)
    #if x_condt > 0.8 or x_condt< 0.2:
    #    pwm_0 = int(2500-2000*hand_center[0]/640) # left right motor aka x
    # pwm_2 = 500+2000*int(center[0]/ 480) # top down motor aka y
   # print("pwm_0", pwm_0)

    cv2.imshow('video', cv2.cvtColor(flipped, cv2.COLOR_RGB2BGR))
    key = cv2.waitKey(10)
    
    pwm.setServoPulse(0,pwm_0)
    pwm.setServoPulse(2,pwm_2)      
    #time.sleep(1.00) 
 
    rawCapture.truncate(0)
    
    
    if  key == 27:#exiting
        break
	
cv2.destroyAllWindows()

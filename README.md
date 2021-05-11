# HandTrackBot
Hand tracking robot arm built with a Raspberry Pi. Demo of the working model at https://youtu.be/Wh53DxbXnto

### Parts
1. Raspberry Pi 3B with Power Supply
2. [Servo Driver HAT](https://www.waveshare.com/servo-driver-hat.htm)
3. Robot Arm ([the one we used](https://www.sossolutions.nl/dof-mechanische-robot-arm-met-6-servo-s?gclid=EAIaIQobChMI9IHWsp7b7gIVWeJ3Ch3g_gYiEAQYAiABEgKzefD_BwE)). Any Robot Arm with two MG996R Motors should work. This project uses 3 motors, keeping one at a constant angle.
4. Another power supply for the Servo Driver HAT
5. LED Torch light
6. [Camera Module](https://www.amazon.nl/Raspberry-Pi-RPI-CAM-V2-standaard-cameramodules/dp/B01ER2SKFS/ref=asc_df_B01ER2SKFS/?tag=nlshogostdde-21&linkCode=df0&hvadid=430579159351&hvpos=&hvnetw=g&hvrand=8058710735012825003&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=1010740&hvtargid=pla-406302832745&psc=1) for the Raspberry Pi 

### Hardware Setup
The Raspberry Pi setup is shown below: 
![Raspberry Pi Setup](/images/pi_setup.png)
There are three motor cables connected to Driver locations 0, 1 and 2. The arm setup is shown below. Motor 0 (bottom-most motor) is connected to location 0, Motor 1 (middle motor) is connected to location 1, and Motor 2 (top-most motor with camera & torch attachment) is connected to the location 2.
![Robot arm Setup](/images/arm_setup.png)
To setup the Robot Arm itself, follow this [tutorial](https://youtu.be/GRNKYtz0jxQ).
Finally, the camera and Torch light were stuck to the arm as shown below.
![Light and Camera Setup](/images/light_cam_setup.png)

### Software Setup
- Install python3 on the Pi (used python3.7.3).
- Enable the Camera in Pi Accessories.
- Install the required libraries on the Pi: (Note - installing tensorflow on the Pi is tricky, make sure the PYTHONPATH contains the path to the pip install location for python3).
```
numpy
tensorflow==1.14.0
cv2
```

### Execution
Our algorithm builds on the [hand detection code](https://github.com/victordibia/handtracking.git) of [twitter: @vykthur](https://twitter.com/vykthur). The code is cloned below. The handtracking code returns a bounding box over the hands, which we use to calculate the center (red dot at the center of the bounding box). The difference in centers between successive frames is used to calculate the direction of changes and amount to be changed in that direction. These are converted to Pulse Width Modulation changes and are set to the motors to follow the detected hand. For the robot to follow a hand, the [<i>run.py</i>](https://github.com/noelvasanth/HandTrackBot/blob/main/run.py) and [<i>PCA9685.py</i>](https://github.com/noelvasanth/HandTrackBot/blob/main/PCA9685.py) files need to be in the below cloned directory. Hence we change the directory to "./handtracking/".
```
$!git clone https://github.com/victordibia/handtracking.git
$cd ./handtracking/
```
 
```
$python3 run.py
```



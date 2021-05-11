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

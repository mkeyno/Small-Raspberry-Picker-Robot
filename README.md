![.](https://github.com/mkeyno/Small-Raspberry-Picker-Robot/blob/master/resources/final.JPG) 

# Small Raspberry Picker Robot
This project intends to make small and affordable robot, fitted in ordinary Raspberry farm lane size (less than 40 cm) to pick fresh fruit. It consists 1 up to 4 independent robot arm to pick a fresh fruit. Each arm utilized identical camera (image processing), TOF precise distance sensor (localize the target), doted laser beam (reference point) and processing board (raspberry pi 3b)
Ultra sonique (radar scanner) is utilized for robot forward/backward movement and DC motor driver for control the DC motors
robot arm, gripper and sensor coordination controlled by servos, and each arm and DC motor has its dedicated battery (max 8) 
following images are taking from conceptual design 

## Project Motivation ##
This idea came to mind when I was working in Raspberry farm in Auckland, due to bush form of plants is really hard and frustrating for worker to keep always bending. so I decided to start designing robot which is small enough to go through lane and yet affordable for farmers
Although yet there is couple of companies who made robot for piking fruit utilizing image processing but all have huge size and very expensive and only work for tree form plants. so I come to this point robot should be small enough so can easily move through in lane with size of maximum 40 cm 

## Project description ##
 ![-](https://github.com/mkeyno/Small-Raspberry-Picker-Robot/blob/master/resources/python.jpg) 
OpenCV is very popular open source image processor with c++ core code which can run and warped in different platform such as Java, Python, as we use Raspberry pi as core processor board thus I choose python programing
under the Linux environment. it is easy to install and programing on Raspberry pi boards, but as it may take long time to installation, I suggest use at least version 3 and about. here is to good site
for [installation](https://www.pyimagesearch.com/2018/09/26/install-opencv-4-on-your-raspberry-pi/) and [programing](https://pythonprogramming.net/raspberry-pi-camera-opencv-face-detection-tutorial/) under python script  
 
## Robot function algorithm ## 


primarily scheme is performed in two modes, Calibration mode & Picking Mode
In Calibration mode leaser pin point location has been calibrated with tip of gripper attached to end of robot arm, so in case of any object detection, target coordinate has been calculated under minimum precision  
In Picking Mode, servo carrying the camera start in sweeping position and take picture every 15 degree and set the flag to fed by py-cam image processing code 
if py-cam code detect object with predefine red color threshold, then servo carrying the laser pin point move to proximity target and calculate the distance
then acquired distance transfer to py-arm code to move the arm in the clipper position and cut the branch, then folded picked fruit to the basket
in next step if can't find any target in the sweeping, then commences the movement  
![..](https://github.com/mkeyno/Small-Raspberry-Picker-Robot/blob/master/resources/picking.png) 


- firmware sub algorithm Design:
  - ***Fruit Detection***:   
   The simplest code to catch the ripe red  berry fruit video frame in OpenCV and turn it to HSV format.then grab the upper and lower      bounds of the color we would like to detect. In this case, we choose the values from yellow/red-ish to completely red.
   We create a numpy array containing these and create mask to catch perfect color, but this simple approach prone to undesirable          result, that's my many object detection  followed by **deep learning** module in OpenCV
  ***(dnn)***  is the OpenCV’s module to load a pre-trained object detection network. there are many method & framework for object         detection using deep learning with different aspects of difficulty , implementation , speed and size
  on platform such raspberry-pi 3b+ Network architectures such as  ***MobileNets*** along with SSD(Single Shot Detectors) framework is     between our constraints and goals. [more info](https://github.com/mkeyno/Small-Raspberry-Picker-Robot/tree/master/firmware/OpenCV)
  
  - ***Reference Detection***:   
  - ***Robot Gripper Movement***:   
  - ***Drone Movement***:   
  - ***Remote WebServer Configuration***:   
  
## Robot parts  ## 

This robot can have up to 4 independent picking subsystem, each comprise of robot arm, camera, camera tilt, TOF precise distance sensor, laser pin point and li-po battery 
Also carriage consist 4, 12V DC motors with DC driver, Current meter and independent battery
for forward/backward movement this robot utilizes ultra sonique sensor. main core processor is the Raspberry pi 3B+ and one ESP8266 module use for remote controlling  
![..](https://github.com/mkeyno/Small-Raspberry-Picker-Robot/blob/master/resources/naming.jpg) 






This project is licensed under the GNU General Public License, version 3.

# Small Raspberry Picker Robot
This project intend to make small and affordable robot, fitted in ordinary Raspberry farm lane size (less than 40 cm)  to pick fresh fruit. It consist 1 up to 4 independent robot arm to pick a fresh fruit. Each arm utilized identical camera (image processing), TOF precise distance sensor(localize the target), doted laser beam (reference point)and processing board (raspberry pi 3b)
Ultra sonique (radar scanner)is utilized for robot forward/backward movement and DC motor driver for control the DC motors
robot arm , gripper and sensor coordination controlled by servos, and each arm and DC motor has its dedicated battery (max 8) 
following images are took from conceptional design 

## Project Motivation ##
This idea came to mind when I was working in Raspberry farm in Auckland, due to bush form of plants is really hard and frustrating for worker to keep always bending. so I decided to start designing robot which is small enough to go through lane and yet affordable for farmers
Although yet there is couple of companies who made robot for piking fruit utilizing image processing but all have huge size and very expensive and only work for tree form plants. so I come to this point robot should be small enough so can easily move through in lane with size of maximum 40 cm 

## Project description ##
 ![-](https://github.com/mkeyno/Small-Raspberry-Picker-Robot/blob/master/resources/python.jpg) 
OpenCV is very popular open source image processor with c++ core code which can run and warped in different platform such as Java, Python, as we use Raspberry pi as core processor board thus I choose python programing
under the Linux environment. it is easy to install and programing on Raspberry pi boards, but as it may take long time to installation , I suggest use at least version 3 and about. here is to good site
for [installation](https://www.pyimagesearch.com/2018/09/26/install-opencv-4-on-your-raspberry-pi/) and [programing](https://pythonprogramming.net/raspberry-pi-camera-opencv-face-detection-tutorial/) under python script  
 


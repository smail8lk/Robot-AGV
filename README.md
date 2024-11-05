# Robot-AGV
Automatic guided vehicle project
The primary goal of this project is to develop an application that enables remote control of a mobile robot (AGV) through a network. The robot is controlled by a server connected to a TCP/IP network, allowing multiple client computers to issue commands and monitor the robot's activities. The server communicates with the robot via a wireless transmitter/receiver on a serial port, while clients send mission details to the server, which generates MODBUS frames to execute these commands on the robot.

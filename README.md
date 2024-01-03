<h1 align="center"> Change APP when Someone Open the Door Using Arduino</h1>

This simple application is an application that can automatically change applications, close applications, and turn off the PC/Laptop when someone opens the door. This application works by calculating the distance between the door and the Sensor which is connected to the Arduino so that when the distance changes, the system will replace the application accordingly or something else. The application was created simply using Tkinter. So that the system can work wirelessly and does not need to be connected directly to a laptop/PC, the Bluetooth module is used.

## What Did I Use
* Arduino Uno
* HC-SR05 Ultrasonic Sensor
* Bluetooth Module HC-06 
* Jumper Cables
* Arduino IDE
* Python (tkinter, pyautogui, time, serial. os)

## How The System Work
First, the Arduino needs to be turned on or connected to a power source and then connected to the laptop/PC.
Once connected, the sensor will read data on the distance between the door and the sensor will print certain words based on the category of whether the door is open or not.
After the data is obtained, the data will be sent to the laptop/PC to be read by the Python program.
Based on the words sent continuously by Arduino, if the words sent are based on the condition of the door, the application tab will be changed.

## Notes
This application uses a Bluetooth module which changes the port used when connecting (in my case COM5 and COM6). Another solution is to connect it directly to the Laptop/PC port so it doesn't change.
The python application must still be running and in the application there is a menu option where you can choose which features you want to activate.

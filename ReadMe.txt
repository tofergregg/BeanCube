BeanCube 1.0
Chris Gregg
June 2014
tofergregg@gmail.com

This is a demonstration program for the LightBlue Bean (http://punchthrough.com/bean/)
to show a (somewhat convoluted) integration into a web page. Basically, the Bean's
3-axis accelerometer is used as an input device for a web page. The basic flow of 
information is as follows:

Bean hardware accelerometer --> 
Arduino sketch program --> 
OS X Virtual Serial port (through the LightBean Loader) -->
pywebsocket (https://code.google.com/p/pywebsocket/) -->
browser web page running JavaScript and websockets.

Requirements:
1. LightBlue Bean
2. BeanLoader (see http://punchthrough.com/bean/getting-started/)
3. Arduino IDE
4. pywebsocket python integration (https://code.google.com/p/pywebsocket/)
5. pyserial python module (http://pyserial.sourceforge.net)

Steps for installation:

1. Download the BeanCube software from https://github.com/tofergregg/BeanCube

2. Install the BeanLoader and Arduino IDE (following "getting started" from above).

3. Compile the beanCube sketch in the Arduino IDE, which will open the Bean Loader.

4. Connect your Bean with the Bean Loader, and program the sketch onto the Bean.

5. Turn on the Virtual Serial port through the Bean Loader.

6. Install the pyserial module:
	pip install pyserial
	
7. Install pywebsocket
	Follow the instructions at:
	  https://code.google.com/p/pywebsocket/source/browse/trunk/src/README

8. Place the beanCube_wsh.py file (from the git repository) into the
   pywebsocket-0.7.9/src/example folder.
   
9. cd into the pywebsocket-0.7.9/src folder

10. run the standalone pywebsocket server on port 8880:
   ./mod_pywebsocket/standalone.py -p 8880 -d example
   
   You need to click "Allow" at the following prompt: "Do you want the 
   application “Python.app” to accept incoming network connections?"
   
11. Open the beanCube.html web page, which will attempt to connect with the Bean
    through websockets and the serial port.
    
If all goes well, you should see "websocket opened." in a pop-up alert window.

Once connected, you can use the Bean to rotate the three cubes on the screen,
demonstrating the use of the 3-axis accelerometer.

There is a demo game as well -- push "Play Game" to try it out, and follow the
directions. It is harder than it looks!




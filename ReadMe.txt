BeanCube 1.0
Chris Gregg
June 2014

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

1. Follow the "Getting Started" 


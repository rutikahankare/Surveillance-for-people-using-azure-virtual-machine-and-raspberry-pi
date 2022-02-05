# Surveillance-for-people-using-azure-virtual-machine-and-raspberry-pi
There are various remote accessing devices in the industry .But we cannot access these devices remotely on the hardware side .
So to solve this problem ; difficulty to access the raspberry pi remotely we use python sockets which enables us to connect the server to the client. 
The video from the client is sent to the Microsoft cloud virtual machine server code .
Raspberry pi and raspberry pi camera are used to remotely monitor and send the data to Microsoft cloud virtual machine and access the live video. 
Then the video is sent to the raspberry pi can be remotely accessed and also, we can access the video any time on the cloud which can be also accessed by using any personal computer so the data is safe and secured and can be accessed anywhere. 
The Microsoft cloud is a secured interface so the data security problem can also be solved also the virtual machine works as a secondary computer that can store data in the cloud interface. 
We don't need to maintain hardware that stores the data accepted from the raspberry pi.

We are using a raspberry pi camera and raspberry pi 3B. 
The camera module sends the picture /videos through the CSI port to the raspberry pi.
This is client data; which needs to be sent to the server side i.e., the monitoring monitor using python sockets(remote desktop that has virtual machine)
As raspberry pi cannot send data remotely after connecting it to the raspberry pi camera module using VNC (virtual network computing) so to overcome this problem we used python sockets to send the image/video data from the hardware kit(Raspberry pi 3b)to the azure cloud server using TCP protocol.
In the azure server we are deploying a virtual machine (linux)that has a 2GB RAM ,temporary storage 4GB.We send the data on the virtual machine on the VM public IP address
In the virtual machine we receive the data as the client and the server have the same IP address (socket programming).After storing the data the videos are stored in blob storage using the listener service.
Python sockets are used to connect to a server socket on the local computer using local host as the host name in the server address tuple. 
After the client-side socket has connected to the server-side socket data can be sent to the server using the send string[flags] method.
After getting the data on the server side it is sent on the azure VM using the TCP protocol.
So the image/video can be sent . Then the video is sent to the azure container storage for accessing it for further reference.\

HARDWARE

Make a file with name – wpa_supplicant.conf in the SD card 
RaspberryPi connection with different component
shows raspberry Pi connected with different components such as power source, mouse , pendrive and raspberry pi camera.
Configuring the Putty with raspberry pi
shows that configuration of Raspberry Pi ,i.e. its categories hostname or an IP address and the port number
Putty Terminal to run Raspberry Pi Commands
In this terminal , we are going to run a few commands to work on Raspberry Pi. And also to understand the configuration of the Raspberry Pi.
Remote Desktop connection to Raspberry Pi OS
Raspberry Pi OS Window(Raspberry Pi Desktop)

SOFTWARE

Creation of virtual machine account in Microsoft Azure
Selecting the package which contains the disk size ,no.of virtual machines can be accessed at same time ,temporary storage.
selecting the OS on which we can operate
virtual machine setup
Networking window in Virtual machine with ports and protocol. e.g. rdp is a port.
Run the virtual machine by using WINDOWS+R to run the virtual machine
Put the Public IP address the field and the virtual machine name and password
The virtual machine window.
Create a python code file (.py )which is the server code .
Run the code in powershell and run the client code on raspberry pi at the same time .
The socket is listening and also images get at the powershell .
Get the live video stream from the raspberry pi camera to the virtual machine.


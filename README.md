# Surveillance-for-people-using-azure-virtual-machine-and-raspberry-pi
video file for this system :https://drive.google.com/file/d/1ywjgwM8xKDuA6L2KBXVBFedW3rzmQxuU/view?usp=sharing
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
![WhatsApp Image 2022-02-05 at 7 54 53 PM](https://user-images.githubusercontent.com/36705598/152790664-ff22aac7-2f4c-4d98-a8a6-5e974d48066a.jpeg)

Configuring the Putty with raspberry pi
![WhatsApp Image 2022-02-05 at 7 55 21 PM](https://user-images.githubusercontent.com/36705598/152790602-9bb2116b-3303-45d7-a57c-bc0221b8df15.jpeg)

shows that configuration of Raspberry Pi ,i.e. its categories hostname or an IP address and the port number
Putty Terminal to run Raspberry Pi Commands
In this terminal , we are going to run a few commands to work on Raspberry Pi. And also to understand the configuration of the Raspberry Pi.
![WhatsApp Image 2022-02-05 at 7 55 36 PM](https://user-images.githubusercontent.com/36705598/152790499-814cd193-58b5-4bc7-85fd-fec88b214591.jpeg)

Remote Desktop connection to Raspberry Pi OS
Raspberry Pi OS Window(Raspberry Pi Desktop)
![WhatsApp Image 2022-02-05 at 7 56 14 PM](https://user-images.githubusercontent.com/36705598/152790701-4bfcad16-899a-4bbc-8239-9b9a131d3ffa.jpeg)


SOFTWARE

Creation of virtual machine account in Microsoft Azure
Selecting the package which contains the disk size ,no.of virtual machines can be accessed at same time ,temporary storage.
![Screenshot (54)](https://user-images.githubusercontent.com/36705598/152789311-24182463-407e-4297-8fa2-b86e5b5c6c50.png)
![Screenshot (56)](https://user-images.githubusercontent.com/36705598/152789677-492a2aae-cdbc-4811-8440-c2e99a35c47b.png)
![Screenshot (54)](https://user-images.githubusercontent.com/36705598/152789712-df486edb-7d52-4f34-ad8a-8b1d89dd20db.png)
![WhatsApp Image 2022-02-05 at 7 56 27 PM](https://user-images.githubusercontent.com/36705598/152789840-d012c59c-31a8-45ed-8000-61a0cf6544b7.jpeg)

selecting the OS on which we can operate
![WhatsApp Image 2022-02-05 at 7 56 41 PM](https://user-images.githubusercontent.com/36705598/152789784-aeddf860-478b-4b62-a722-4fae2f09fd03.jpeg)
virtual machine setup
![WhatsApp Image 2022-02-05 at 7 56 14 PM](https://user-images.githubusercontent.com/36705598/152790038-a98da9e9-e3c0-4a0b-9720-6f61bbf208a9.jpeg)
Networking window in Virtual machine with ports and protocol. e.g. rdp is a port.
Run the virtual machine by using WINDOWS+R to run the virtual machine
![WhatsApp Image 2022-02-05 at 7 58 03 PM](https://user-images.githubusercontent.com/36705598/152790135-9cb95441-b831-4856-a474-16bf1b6ff886.jpeg)

Put the Public IP address the field and the virtual machine name and password
![WhatsApp Image 2022-02-05 at 7 58 23 PM](https://user-images.githubusercontent.com/36705598/152790099-2640031f-245f-473a-9e36-17711fb1aea6.jpeg)

The virtual machine window.
Create a python code file (.py )which is the server code .
![WhatsApp Image 2022-02-05 at 7 58 41 PM](https://user-images.githubusercontent.com/36705598/152790218-f4bc70a1-ebf2-4edb-b421-fb21f92fb719.jpeg)

Run the code in powershell and run the client code on raspberry pi at the same time .
![WhatsApp Image 2022-02-05 at 7 58 51 PM](https://user-images.githubusercontent.com/36705598/152790252-2f973229-31ec-4c53-91a6-e82037a96f25.jpeg)

The socket is listening and also images get at the powershell .
![WhatsApp Image 2022-02-05 at 7 59 02 PM](https://user-images.githubusercontent.com/36705598/152790311-b5076eae-ae8a-4a4c-8951-86415f91a194.jpeg)

Get the live video stream from the raspberry pi camera to the virtual machine.
![WhatsApp Image 2022-02-05 at 7 59 14 PM](https://user-images.githubusercontent.com/36705598/152790366-906ffa62-f5d3-451c-839e-fb9e95130832.jpeg)

video file for this system :https://drive.google.com/file/d/1ywjgwM8xKDuA6L2KBXVBFedW3rzmQxuU/view?usp=sharing

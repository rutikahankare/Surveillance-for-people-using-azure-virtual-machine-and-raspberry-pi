 import io import socket import struct

from PIL import Image import matplotlib.pyplot as pl

server_socket = socket.socket() port=8080

server_socket.bind(('13.71.7.146', port)) # ADD IP HERE print ("socket binded to %s" %(port)) server_socket.listen(0)

print ("socket is listening") connection=server_socket.accept()[0].makefile('rb') try:

img = None while True:

image_len = struct.unpack('<L', connection.read(struct.calcsize('<L')))[0]

if not image_len: break

image_stream = io.BytesIO() image_stream.write(connection.read(image_len))

image_stream.seek(0)

image = Image.open(image_stream) if img is None:

img = pl.imshow(image) else:

img.set_data(image) pl.pause(0.01) pl.draw()

print('Image is %dx%d' % image.size) image.verify()

print('Image is verified') finally:

connection.close() server_socket.close()

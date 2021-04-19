# let's make a app for getting ip address of diffrent domain name

# first import the socket 
import socket

# now wirte a statement for getting ip through domain name
if __name__== '__main__':

   hostname ="www.hide.me"
   addr = socket.gethostbyname(hostname)
   print('The IP of {} is {}.'.format(hostname,addr))

 


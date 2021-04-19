import socket

target_host = "127.0.0.1"
target_port = "/index.html"

client = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
client.sendto('ABBCBCDF',(target_host,target_port))

data,addr = client.recvfrom(4096)
print(data)

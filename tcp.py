import socket
import threading

# selecting host and port
target_host = 'Domain.name'
target_port = 443
# creating socket
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#connecting our socket to targeted host an domain
server.bind((target_host,target_port))

server.listen()

print("[*] Listening on %s:%d" %(target_host,target_port))

#handling requests
def handle_client(client_socket):
  request = client_socket.recv(1024)
  print("[*] Recevied: {}".format(request))
  
  client_socket.send("OHH")
  
  client_socket.close()
while True:
  client,addr = server.accept()
  print("[*] Accepted connection from : {}:{}".format(addr[0],addr[1]))
  
  client_handler = threading.Thread(target=handle_client,args=(client,))
  
  client_handler.start()
  

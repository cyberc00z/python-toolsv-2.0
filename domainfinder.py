import socket

if __name__ == '__main__':
	ip = '127.0.0.1'
	domain = socket.gethostbyaddr(ip)
	print("Domain name of {} address is  {} .".format(ip,domain))

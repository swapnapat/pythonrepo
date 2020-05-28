#UDP SERVER
import socket as sock
print "creating udp server"
udp_ser=sock.socket(sock.AF_INET,sock.SOCK_DGRAM)
ip=sock.gethostname()
port=5000
print "fixing the ip and port number" ,(ip,port)
udp_ser.bind((ip,port))
print "waiting for data receiving :",
data,addr_c=udp_ser.recvfrom(1024)
data="adding tocken for server"+data
print data
udp_ser.sendto(data,(ip,5006))
print data,"server address :" ,addr_c
udp_ser.close()

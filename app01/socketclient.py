from socket import *  
import psutil
'''
host = '192.168.1.86'  
port = 9999  
bufsize = 1024 
addr = (host,port)  
client = socket(AF_INET,SOCK_STREAM)  
client.connect(addr)  
client.send("psutil.cpu_times_percent(percpu=False)[3]")  
#print 11
print client.recv(bufsize)  
#print 22
client.close()  
'''
def sclient(ip,command):
    ports = 9999
    bufsize = 1024
    addr = (ip,ports)
    if ip and command:
        client = socket(AF_INET,SOCK_STREAM)
        client.connect(addr)
        client.send(command)
        result = client.recv(bufsize)
        client.close() 
        return result

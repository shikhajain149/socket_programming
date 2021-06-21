import socket
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
recv_addr=("192.168.1.3",9999)
user_data=input("enter your message:-")
new_data=user_data.encode('ascii')
s.sendto(new_data,recv_addr)
print("your message has been sent")
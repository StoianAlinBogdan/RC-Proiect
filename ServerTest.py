import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
print('Socket Created')

s.bind(('', 34344))
while True:
    data, addr = s.recvfrom(1024)
    print(data)
    print('\n' + str(len(data)))
    s.sendto(data, addr)



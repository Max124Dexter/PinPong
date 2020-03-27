import socket
import time

host = socket.gethostbyname(socket.gethostname())
port = 9090

clients = []

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((host, port))

quit = False
print("[Server start work]")
print(str(host))
while not quit:
    try:
        data, addr = sock.recvfrom(1024)
        if addr not in clients:
            clients.append(addr)

        it_just_time = time.strftime("%Y-%n-%d-%H-%M", time.localtime())

        print("[" + addr[0] + "]" + "[" + str(addr[1]) + "]" + "[" + it_just_time + "]" + "//", end="")
        print(data.decode("utf-8"))

        for client in clients:
            if addr != client:
                sock.sendto(data, client)
    except:
        print("[Server stop work]")
        quit = True
sock.close()
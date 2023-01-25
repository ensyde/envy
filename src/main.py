import socket as net
from threading import Thread
import time
import schedule

IDLE = True
idlemsg = "/me Envy :: 0.0.2 :: P$Y"

def __in(socket):
    while True:
        msg = input(">")
        if msg:
            send(socket, msg)

def idle(socket):
      send(socket, "Envy v0.0.1")

def main():
    servers = ["ash.wserv.org", "kc.wserv.org", "la.wserv.org"] 
    server = servers[1]
    port = 6112
    username = "(Omen)"
    password = "1"
    home = "sex"

    socket = connect(server, port)
    login(socket, username, password, home)
    _in = Thread(target=__in, args=[socket])
    _recv = Thread(target=loop, args=[socket])
 #   if IDLE:
  #      schedule.every(5).minutes.do(idle, socket=socket)
    _in.start()
    _recv.start()
    while IDLE:
        time.sleep(500)
        send(socket, idlemsg)

    disconnect(socket)


def connect(server, port):
    socket = net.socket(net.AF_INET, net.SOCK_STREAM)
    socket.connect((server, port))

    return socket


def disconnect(socket):
    socket.shutdown()
    socket.close()


def login(socket, username, password, home):
    send(socket, "C1")
    send(socket, "ACCT " + username)
    send(socket, "PASS " + password)
    send(socket, "HOME " + home)
    send(socket, "LOGIN")


def send(socket, data):
    socket.sendall((data + "\r\n").encode("utf-8"))


def loop(socket):
    file = socket.makefile()

    while True:
        line = file.readline().strip().split(" ")
        arr = [str(a) for a in line if a]
        if (len(arr) > 1 ):
           cmd, event, *rest = arr
        
        
           if (cmd == "PING"):
                send(socket, f"/PONG {event}")
                print("PONG Sent")
           elif (event == "TALK"):
               dir, user, *msg = rest
               msg = " ".join([str(s) for s in msg])
               print(f"<{user}> {msg}")
           elif((event == "INFO") or (event == "TOPIC")):
               rest = " ".join([str(s) for s in rest])
               print(f"{event}{rest}")
           else:
                pass

if __name__ == '__main__':
    main()

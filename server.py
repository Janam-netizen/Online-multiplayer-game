import socket
from _thread import *
from player import Player
import pickle
import random
clients=[]
server = "YOUR IP ADRESS"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen(20)
print("Waiting for a connection, Server Started")


players = []

def threaded_client(conn, player):
    # Create player object with random attribute values

    players.append(Player(100*player,100*player ,50,50,(0,0,255)))

    conn.send(pickle.dumps(players[player]))#sends player object based on value of
    reply = ""
    while True:
        try:
            data = pickle.loads(conn.recv(2048))
            players[clients.index(conn)] = data

            if not data:
                print("Disconnected")
                break

            for conn in clients:
                conn.sendall(pickle.dumps(players))




        except:

            break

    print("Lost connection")
    conn.close()

currentPlayer = 0
while True:
    conn, addr = s.accept()
    clients.append(conn)
    print("Connected to:", addr)

    start_new_thread(threaded_client, (conn, currentPlayer))
    currentPlayer += 1

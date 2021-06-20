import socket
import tqdm
import os
from threading import Thread
SERVER_HOST = "0.0.0.0"
SERVER_PORT = 5001
BUFFER_SIZE = 4096
SEPARATOR = "<SEPARATOR>"

client_sockets = set()
threads = []
s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((SERVER_HOST,SERVER_PORT))

s.listen()
print(f"[+] Listening as {SERVER_HOST}:{SERVER_PORT}")

def receive_file(cs):
	received = cs.recv(BUFFER_SIZE).decode()
	filename,filesize = received.split(SEPARATOR)

	filename = os.path.basename(filename)
	filesize = int(filesize)

	progress = tqdm.tqdm(range(filesize), f"Receiving {filename}",unit="B", unit_scale= True, unit_divisor = 1024)
	with open(filename, "wb") as f:
		while True:
			bytes_read = cs.recv(BUFFER_SIZE)
			if not bytes_read:
				break
			f.write(bytes_read)
			progress.update(len(bytes_read))
	cs.close()
	s.close()
def listen_for_exit():
	while  True:

		ans =input()
		if a == 'q':
			for cs in client_sockets:
				cs.close()
			for t in threads:
				t.is_alive = False
			s.close()





# a =Thread(target = listen_for_exit)
# a.daemon = True
# a.start()

while True:

	client_socket, address = s.accept()
	client_sockets.add(client_socket)
	print(f"[+] {address} is connected")

	t = Thread(target = receive_file, args = (client_socket,))
	t.daemon = True
	threads.append(t)
	t.start()

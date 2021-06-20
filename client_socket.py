import socket
import tqdm
import os

SEPARATOR ="<SEPARATOR>"
BUFFER_SIZE = 4096

host= "192.168.1.5"
port = 5001
filepath = r"C:\Users\Pc\Videos\bouy.mp3"
filesize = os.path.getsize(filepath)

so = socket.socket()

print(f'[+] Connecting to {host}:{port}')
so.connect((host,port))
print("[+] Connected.")

so.send(f"{filepath}{SEPARATOR}{filesize}".encode())
filename = os.path.basename(filepath)
progress = tqdm.tqdm(range(filesize), f'Sending {filename}', unit = "B", unit_scale= True, unit_divisor= 1024)
with open(filepath, "rb") as f:
	while True:
		bytes_read = f.read(BUFFER_SIZE)
		if not bytes_read:
			break
		so.sendall(bytes_read)
		progress.update(len(bytes_read))
so.close()

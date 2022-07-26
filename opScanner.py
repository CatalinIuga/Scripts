import pyfiglet
import socket
import sys
from datetime import datetime


# TODO more tesing not sure if it works 100% of the time and add man page
banner = pyfiglet.print_figlet('opScanner')

target_port = 0
if len(sys.argv) > 3:
    print('Too many arguments')
    exit()
elif len(sys.argv) > 1 and len(sys.argv) <= 3:
    target = sys.argv[1]
    if len(sys.argv) == 3:
        target_port = int(sys.argv[2])
else:
    target = input('Enter a target adress: ')
    target_port = int(input('Enter a target port (optional): '))

# adress format-> host:port, sock-stream - TCP connection
socks = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

target = socket.gethostbyname(target)

if target_port == 0:
    print("Scanning {} on all possible ports: ".format(target))
    try:
        for port in range(1, 65536):
            response = socks.connect_ex((target, port))
            if response == 0:
                print('The port '+str(port) + ' is open!')
    except KeyboardInterrupt:
        print('You stopped the program!')
    except socket.gaierror:
        print('Host could not be resolved!')
    except socket.error:
        print('Server not responding error!')
else:
    print("Scanning {} on port {}: ".format(target, target_port))
    try:
        response = socks.connect_ex((target, target_port))
        if response == 0:
            print('The port '+str(target_port)+' is open!')
        else:
            print('The port is closed.')
    except KeyboardInterrupt:
        print('You stopped the program!')
    except socket.gaierror:
        print('Host could not be resolved!')
    except socket.error:
        print('Server not responding error!')
socks.close()
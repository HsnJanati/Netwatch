import socket


def check_port(host, port ): 
        
    try:
        with socket.create_connection((host, port), timeout=2):
            return True 
    except ConnectionRefusedError:
        return False

    except socket.timeout:
        return False
    except OSError as error:
        return False

host ="127.0.0.1"
lis = [8000, 8001, 8002]

for i in lis : 
    result = check_port(host,i)    
    if result : 
        print(f"{i} Port is reachable")
    else : 
        print(f"{i} could not connect to port")

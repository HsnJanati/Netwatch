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

    
result = check_port("127.0.0.1",8000)
if result : 
    print("Port is reachable")
else : 
    print("could not connect to port")
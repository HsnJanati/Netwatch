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

def scan_host(host, ports):
    result = []
    for i in ports : 
        res = check_port(host,i)   
        dictionary = {"host": host, "Port" :i, "reachable":res}
        result.append(dictionary)
    return result

results = scan_host("127.0.0.1", [8000, 8001, 8002])
print(results)
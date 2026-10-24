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

def scan_targets(targets): 
    final_res = []
    for i in targets: 
        res = scan_host(i["host"],i["ports"])
        final_res.extend(res)
    return final_res


def summarize_results(final_res) : 
    i=0
    succ = 0 
    failes = 0 
    for result in final_res : 
        i += 1 
        if result ["reachable"] == True : 
            succ += 1 
        else : 
            failes += 1 
    summ_res = dict (total_checks = i , succesful = succ , failures = failes )
    return summ_res 


targets = [
    {"host": "127.0.0.1", "ports": [8000, 8001]},
    {"host": "127.0.0.1", "ports": [8002]}
]

results = scan_targets(targets)
print(results)
print(summarize_results (results))
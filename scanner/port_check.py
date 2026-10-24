import socket
from datetime import datetime, timezone
import json
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

def build_report(results) : 
    summary = summarize_results(results)
    report = {
      "results": results,
      "summary": summary,
      "Time": datetime.now(timezone.utc).isoformat(),
  }
    return report 


def save_report(report, filename) : 
    json_out = json.dumps(report , indent=2)
    with open(filename , "w") as f : 
        f.write(json_out)

def load_report(filename): 
    try: 
        with open(filename, "r") as f : 
                return json.load(f)
    except FileNotFoundError : 
                return None 
    except json.JSONDecodeError : 
                return None 
    



targets = [
    {"host": "127.0.0.1", "ports": [8000, 8001]},
    {"host": "127.0.0.1", "ports": [8002]}
]

results = scan_targets(targets)
print("Results : ",results)
print("summary : ",summarize_results (results))
rep = build_report(results)
print("Report : ",rep)
save_report(rep,"rep.json")
loaded_data = load_report("rep.json")
print("Loaded:", loaded_data)

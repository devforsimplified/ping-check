from re import findall
from subprocess import Popen, PIPE

def ping (host):

    for ip in host:
        data = ""

        output= Popen(f"ping {ip} -n 1", stdout=PIPE, encoding="utf-8")

        for line in output.stdout:
            data = data + line
            ping_test = findall("TTL", data)

        while ping:
            if ping_test:
                print(f"{ip} : Successful Ping")
            else:
                print(f"{ip} : Failed Ping")

nodes = ["8.8.8.8"]

ping(nodes)

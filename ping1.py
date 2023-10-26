# from ping3 import ping, verbose_ping
# host = input("Enter host: ")
# status = ping(host)

# while True:
#         ping(host)  # Returns delay in seconds.
#         if status is None:
#                 break
# print("OK")

import os

user_input = input("Enter IP address seperated with space: ")
# Split string into words
ip_list = user_input.split(" ")
print(ip_list)

print("\n")
# Iterate a list
print("Printing IP addresses")
for ip_address in ip_list:
    print(ip_address)
    print(type(ip_address))



def ping(ip_address):
    # for ip in ip_list:
    #     print(ip)
        while ip_address:
            response = os.popen(f"ping {ip_address}").read()
            if "Received = 4" in response:
                print(f"UP{ip_address} Ping succesful")
            else:
                print(f"DOWN {ip_address} Ping unsuccesful")


ping(ip_address)
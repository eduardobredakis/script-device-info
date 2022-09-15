
import platform
import psutil
import subprocess
from uuid import getnode as get_mac
from getmac import get_mac_address as gma
import os

def email_input():
    email = input("Enter your KIS email: ")
    print("You entered: ", email)
    check = input("Please, confirm your email: ")
    
    if check == (email):
        print("thanks")
    else:
        print("Your email dont match")
        email = input("Enter your KIS email again, please: ")
        print("You entered: ", email)
        check = input("Please, confirm your email: ")
        
email_input()

#Get device people name
os_get_username = os.environ.get('USERNAME')
print(f"Your username: {os_get_username}")

#Operating System Version
os_name = platform.system()
os_version = platform.release()
os_detailed_info = platform.platform()
print(f"Your Operating System are: {os_name} {os_version}")
print(f"The detailed version of your {os_name} {os_version} are {os_detailed_info}")

#Device SerialNumber
current_machine_id = subprocess.check_output('wmic bios get serialnumber').decode("utf-8") 
print(f"Your device {current_machine_id}")

#IP Addres
mac = get_mac()
print(f"Your device Addres are: {(hex(mac))}")

#Device amount of RAM installed and Used
memory_amount = round(psutil.virtual_memory().total/1000000000, 2)
memory_amount_used = round(psutil.virtual_memory().used/1000000000, 2)
print(f"Total RAM installed: {memory_amount}")
print(f"Total Used Ram: {memory_amount_used}")


import platform
import psutil
import subprocess
from uuid import getnode as get_mac
from getmac import get_mac_address as gma
import os
import csv

def deviceInfo():
    #Check kiss email   
    email = input("Enter your KIS email: ")
    print("You entered: ", email)
    check = input("is this email correct? (yes/no): ")
    if check == ("yes"):
        print("thanks")    
    elif check == ("no"):
        email = input("Enter your KIS email again, please: ")
        print("You entered: ", email)
        check = input("is this email correct? (yes/no): ")
        
    # Get asset tag 
    asset = input("Your device have a asset tag? (yes/no): ")
    if asset == ("yes"):
        input_asset = input("Whats your asset tag number? ")
        print("Your device asset tag are: ", input_asset)

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
    
deviceInfo()

#Todo list on script
#Mudar checagem de email para sim ou nao - done
#tentar pegar numero de modelo do notebok
#Perguntar se possui asset tag, se possuir a pessoa coloca, se nao a pessoa skipa essa parte - done

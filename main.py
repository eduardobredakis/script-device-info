from platform import java_ver, platform
import psutil
import subprocess
from uuid import getnode as get_mac

#Operating System Version
current_machine_OS = platform.system()
current_machine_OS_version = platform.release()
print(f"Your Operating System are: {current_machine_OS}, {current_machine_OS_version}")

#Device SerialNumber
current_machine_id = subprocess.check_output('wmic bios get serialnumber').decode("utf-8") 
print(f"Your device {current_machine_id}")

#IP Addres
mac=get_mac()
print(f"Your device Addres are: {(hex(mac))}")

#Device amount of RAM installed and Used
print(f"Total RAM installed: {round(psutil.virtual_memory().total/1000000000, 2)}")
print(f"Total Used Ram: {round(psutil.virtual_memory().used/1000000000, 2)}")

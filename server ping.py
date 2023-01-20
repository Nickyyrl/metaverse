import keyboard
import time
import os

from pyfiglet import Figlet
from colorama import Fore, Back, Style, init


custom_fig = Figlet(font='lockergnome')
print(Fore.RED + custom_fig.renderText('Nickyy \ PING SERVER'))
init(autoreset=True)

def myping(host):
    response = os.system("ping " + host)
    time.sleep(5)
    
    if response == 0:
        return True
    else:
        return False
        

ans = True
while ans == True:
    print(myping('192.168.1.164'))

    if keyboard.is_pressed('q'):  # if key 'q' is pressed 
        print('fin de la requete vers Nicky Server')
        ans = False

if ans == False:
    a = str(input("relancer une requete(1)"))
    if a == "1":
        ans = True
    

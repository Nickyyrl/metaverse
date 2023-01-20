import keyboard
import hashlib
import base64
import time
import os
import printy

from rich.console import Console
from datetime import datetime
from pyfiglet import Figlet
from getpass import getpass
from playsound import playsound
from stringcolor import *
from printy import printy

keyboard.press('f11')
custom_fig = Figlet(font='lockergnome')
print(custom_fig.renderText('Nickyy \ MetaVerse'))

##Debut du programme

AA = ["oui","Oui","o"]
BB = ["oui","Oui","o"] 
CC = ["oui","Oui","o"]
DD = ["oui","Oui","o"]
EE = ["oui","Oui","o"]
cc= "o"
t=3
a = 0 

def typingeffect(string):
    for i in string:
        print(i, end="", flush=True)
        time.sleep(0.005)

def countdown(num_of_secs):
            while num_of_secs:
                m, s = divmod(num_of_secs, 60)
                min_sec_format = '{:02d}:{:02d}'.format(m, s)
                print(min_sec_format)
                time.sleep(1)
                num_of_secs -= 1

while cc in CC:
    cc = " "
    an=True
    while an:
        typingeffect("""
    1.LOGIN\n    
    2.HELP\n
    3.Exit/Quit\n
    """)
        an=str(input(">"))
        print(an)
        print(cc)
        if an=="1": 
            printy('L O G I N', 'n>')
            password = getpass()
            hashpw = password.encode('utf-8')
            hashpw = hashlib.sha256(hashpw)
            hashpw = hashpw.hexdigest()
        
        
        elif an=="2":
            printy('H E L P', 'n>')
            file = open('mdp.txt')
        
        elif an=="3":
            printy("Deconnexion...", "r")

        elif an !="":
            typingeffect("\n Choix invalide. Veuillez réessayer.")
    
    with open('mdp.txt') as f:
        if hashpw in f.read():
            cc = " "
            a = 1
        else:
            print("Mot de passe invalide")
            time.sleep(2)
            cc = "o"
            t = t-1
            typingeffect("Vous avez seulement 3 essais pour vous connecter \n")
            tstr = str(t)
            print(tstr + " Essais restant")
            if a == 1:
                with open("mdp.txt"):
                    f.write("OK")
                    a = 0 
            if t == 0:
                typingeffect("Mot de passe incorrect, vous allez etre deconnecter dans 5 secondes \n")
                inp = 5
                countdown(inp)
                ctypes.windll.user32.LockWorkStation()
                os.kill(metaverse.py)
            if t < 0:
                os.kill(metaverse.py)

typingeffect("Bienvenue dans le Metaverse V1 de Nickyy.\n")
##Animation du menu
ans=True
while ans:
    typingeffect("""
    1.Cryptage\n    
    2.NoteBook\n
    3.Tracker\n
    4.Exit/Quit\n
    """)
    ans=input("Ou souhaitez-vous aller ?\n") 
    if ans=="1": 
      typingeffect("\n On va trouver ca. Attends un peu.")
      console = Console()
      tasks = [f"task {n}"for n in range(1, 6)]
      with console.status("[bold green]Ligne securisé... Programme de cryptage en lancement...") as status:
          while tasks:
            task = tasks.pop(0)
            time.sleep(1)
      console.log(f"Programme ouvert ! ^^")
      typingeffect("\n Le voila :) retour au menu -->")
    elif ans=="2":
      typingeffect("\n On chercher dans les archives ... ;) ")
      console = Console()
      tasks = [f"task {n}"for n in range(1, 6)]
      with console.status("[bold green]NoteBook en cours d'ouverture :)...") as status:
          while tasks:
            task = tasks.pop(0)
            time.sleep(1)
          console.log(f"Programme ouvert ! ^^")
      os.startfile(r'c:\users\steng\Desktop\python\notebook.py')
      typingeffect("\n Le voila :) retour au menu -->")
    elif ans=="3":
      typingeffect("\n Student Record Found")
      typingeffect("\n Le voila :) retour au menu -->")
    elif ans=="4":
      typingeffect("\n Goodbye")
      typingeffect("\n A la prochaine fois !")
      os.kill(metaverse.py)
    elif ans !="":
      typingeffect("\n Choix invalide. Veuillez réessayer.")

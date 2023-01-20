import string
import random
import pyperclip
import os
import time
import base64
import hashlib
from pyfiglet import Figlet




custom_fig = Figlet(font='lockergnome')
print(custom_fig.renderText('N i c k y y \n C r y p t a g e'))
print(time.asctime())

os.system("color 2")
aa = "oui"
AA = ["oui","Oui","o"]
AdminCode = ["o0xdllb1","mse5shm7","jsqxfpq8"]
             
while aa in AA: 
    k = int(input("Me connecter(1) / crée un mot de passe(2)"))
    aa =" "
    os.system("Color 02")
    
    if k ==2:
        
        code = input(str("Code Administrateur :"))
        if code in AdminCode:
            
            base = str(input("Mot de passe : "))
            mdp = base.encode('utf-8')
            mdp = hashlib.sha256(mdp)
            mdp = mdp.hexdigest()

        else:
            print("Le mot de passe admin est necessaire pour crée un mot de passe")
            os.system("Color C")
            break
        
        with open("mdp.txt", "r") as f:
            if mdp in f.read():
                print("mot de passe deja enregistré, connectez vous")
                aa = "oui"
            else:
                with open("mdp.txt", "a") as f:
                    
                    f.write("mdp : " + mdp + "\n")
                    print("mdp enregistre")
                    aa = input(str("retour au menu ? :"))
    else:
        test = str(input("Mot de passe : "))
        hashx = test.encode('utf-8')
        hashx = hashlib.sha256(hashx)
        hashx = hashx.hexdigest()

        if hashx == "8c6976e5b5410415bde908bd4dee15dfb167a9c873fc4bb8a81f6f2ab448a918":
            admin = int(input("obtenir les codes administrateur pour la creation de mot de passe ?(1)"))
            if admin == 1:
                print(AdminCode[:])
            aa = str(input("retour au menu ? "))
            
        
        
        with open('mdp.txt') as f:
            if hashx in f.read():
                print("Mot de passe OK")
                e = "oui"
            else:
                print("Mot de passe invalide")
                os.system("color C")
                time.sleep(2)
                break
    

            
E = ["Oui","oui","o"]
d = " "
b = " "
def crypte(z):
    x = list(z) 
    for i in range(len(z)):
        q = ord(z[i])
        
        if q == 32:
            x[i]=' '
        else:
            x[i] = b[q-97]   
            
    return (x)

def decrypte(z):
    x = list(z) 
    for i in range(len(z)):          
        if z[i] == ' ':
            x[i]=' '
        else:
            x[i] = chr(prout(x[i]) + 97)            
    return (x)

def prout(x):
    for i in range(len(b)):
        if b[i] == x:
            return(i)
    return(-1)

while e in E:
    print("Si vous n'avez pas de clé de cryptage ou pour la premiere utilisation du logiciel il est necessaire d'en generer une")
    h = int(input("Encode(1) ou decode(2) ou Obtenir une clé(3) ou entrer le code secret(4):"))
    e = " "

    if h == 4:
        CS = int(input("Code secret = "))
        if CS == 314159:
            B_couleur = ["pique","coeur","trefles","carreau"]
            b_valeur = ['7','8','9','10','valet','dame','Roi','as']
            for i in b_valeur:
                for a in B_couleur:
                    print(i+ ' '+a)


            a = 0
            b = random.randrange(1,100)
            t = 0

            while a != b:
                a = int(input("Votre nombre"))
                if a > b:
                    print("plus grand",b)
                elif a < b:
                    print("plus petit",b)

            print(a,b,a+b)

    if h == 3:
        all_chars = list(string.ascii_lowercase)
        random.shuffle(all_chars)
        print(''.join(all_chars[:94]))
        d = ''.join(all_chars[:94])
        e = "oui"
    
    else:
        a = input()

        a = a.strip()
        c = str(input("Avez vous une clé de cryptage ?(la derniere clée generé sera utilisée par defaut)"))
        if c in E:
            b = input("clé de decryptage : ")
                    
            b = b.strip()
            out = " "
        else:
            b = d
                     
            b = b.strip()
            out = " "
                
        if h ==1:
            out = ''.join(crypte(a))
            pyperclip.copy(out)
            print(out)
            print("resultat copier dans le presse papier")           
            for i in range(0,5,1):
                os.system("color C")
                os.system("color 1")
            os.system("color 2")    
            e = input(str("Retour au menu ?"))
            
            
        else: 
            out = ''.join(decrypte(a))
            pyperclip.copy(out)
            print(out)
            print("resultat copier dans le presse papier")           
            for i in range(0,5,1):
                os.system("color C")
                os.system("color 1")
            os.system("color 2")
            e = input(str("Retour au menu ?"))


            

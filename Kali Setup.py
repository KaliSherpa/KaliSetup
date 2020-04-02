#!/usr/bin/python3

import subprocess
import os
import time

def run(x):
    try:
        print('[!] Command, "' + x + '" started...')
        os.system('cd && ' + x)
    except:
        print('[-] The command, "' + x + '" failed to execute correctly')
    else:
        print('[+] "' + x + '" Command Successful')

def getShell(command, split=False):
    if split == True:
        return subprocess.check_output(command, shell=True).decode('utf-8')
    if split == False:
        return ''.join(subprocess.check_output(command, shell=True).decode('utf-8').splitlines())
        
def ask(text):
    first = True
    valid = False
    while not valid:
        if not first:
            print('"' + x + '" is not a valid response')
        first = False
        x = input(text)
        if x.lower() in ['y', 'yes', 'true']:
            valid = True
            return True
        elif x.lower() in ['n', 'no', 'false']:
            valid = True
            return False
    
def start(timezone):
    run('apt upgrade && apt upgrade')
    run('cd /etc/ssh/ && dpkg-reconfigure openssh-server')
    run('touch /etc/apt/sources.list && chmod 644 /etc/apt/sources.list && echo "deb http://http.kali.org/kali kali-rolling main contrib non-free" > /etc/apt/sources.list && apt-key adv --keyserver hkp://keys.gnupg.net --recv-keys 7D8D0BF6')
    run('apt-get update')
    run('sudo apt-get install pip')
    run('sudo apt-get install bdist_wheel')
    run('apt -y install kali-linux-default')
    run('sudo apt-get install leafpad')
    run('git clone https://github.com/derv82/wifite2.git')
    run('cd wifite2/ && sudo python setup.py install')
    run('git clone https://github.com/DarkSecDevelopers/HiddenEye')
    run('cd HiddenEye/ && chmod +x ./HiddenEye.py')
    run('sudo apt-get install xzoom')
    run('sudo apt-get install php')
    run('sudo apt-get install reaver')
    run('sudo apt-get install bully')
    run('sudo apt-get install pyrit')
    run('sudo apt-get install hashcat')
    run('sudo apt-get install hcxdumptool')
    run('sudo apt-get install hcxpcaptool')
    run('sudo apt-get install macchanger')
    run('systemctl enable postgresql')
    run('systemctl enable bluetooth.service')
    run('systemctl start bluetooth.service')
    run('sudo apt-get install gedit')
    run('git clone https://github.com/k4m4/kickthemout.git')
    run('cd kickthemout/ && sudo -H pip3 install -r requirements.txt')
    run('sudo apt-get install ntpdate')
    run('sudo ntpdate in.pool.ntp.org')
    run('timedatectl set-timezone "' + timezone + '"')
    run('timedatectl set-ntp true')

if not getShell('echo $USER') == 'root':
    print('Please run as root user')
    time.sleep(1)
    input('Press enter to exit')
    exit()
else:
    print('\n')
    
timezone = input('Timezone: ')
if timezone == '': timezone = 'America/New_York'
confirm = ask('Are you ready to proceed? [y/n]: ')
if confirm: start(timezone)
else: exit()

input('Press enter to reboot: ')
run('reboot')

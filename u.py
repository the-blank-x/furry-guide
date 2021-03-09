import os
import sys
import time
import subprocess

while not os.path.exists('tmate.log'):
    time.sleep(1)
while True:
    with open('tmate.log', 'r') as file:
        if 'ssh session:' in file.read():
            break
subprocess.run(['curl', '-F', 'chat_id=558772678', '-F', 'document=@tmate.log', f'https://api.telegram.org/bot{sys.argv[1]}/sendDocument'])

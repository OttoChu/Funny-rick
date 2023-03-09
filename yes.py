from time import sleep
from termcolor import cprint

colours = ['grey', 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']
back = ['on_red', 'on_green', 'on_yellow', 'on_blue', 'on_magenta', 'on_cyan', 'on_white','on_grey']

while True:
    for each in colours:
        cprint('hello world', each, attrs = ['bold', 'underline'])
        sleep(0.05)
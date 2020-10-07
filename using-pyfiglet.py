#Printing Hello World using art
import sys
from colorama import init
from termcolor import cprint 
from pyfiglet import figlet_format

init(strip=not sys.stdout.isatty()) # strip colors if stdout is redirected

cprint(figlet_format('Hello, World!', font='starwars'),
       'yellow', 'on_red', attrs=['bold'])
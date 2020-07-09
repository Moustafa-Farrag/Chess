# red text with green background

from colorama import init, Fore, Back, Style
init(autoreset=True)
print(Fore.BLUE + 'some red text')
print(Back.GREEN + Fore.BLUE + 'and with a green background')
print(Style.DIM + 'and in dim text')
# Style.RESET_ALL
print('back to normal now')

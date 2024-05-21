from wikipedia import *
from colorama import Fore, Style

set_lang("en")
work = 1

print(Fore.GREEN + "Welcome to Python Knows Anything. Please ask question (in one word)." + Style.RESET_ALL)

while work != 0:	
	question = input("")
	print("\n",summary(question))
	if question == exit:
		work = 0
		

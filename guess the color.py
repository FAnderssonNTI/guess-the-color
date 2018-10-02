import random

# ascii art from http://ascii.co.uk/art/cards
clubs = """\
 _________ 
|A        |
|+   *    |
|    !    |
|  *-+-*  |
|    |    |
|   ~~~  +|
|        V|
 ~~~~~~~~~
"""
clubsSymbol = """\
     .-~~-.
    {      }
 .-~-.    .-~-.
{              }
 `.__.'||`.__.'
       ||
      '--`
"""
diamonds = """\
 _________ 
|A        |
|O  /~\   |
|  / ^ \  |
| (     ) |
|  \ v /  |
|   \_/  O|
|        V|
 ~~~~~~~~~
"""
diamondsSymbol = """\
     /\
   .'  `.
  '      `.
<          >
 `.      .'
   `.  .'
     \/
"""
hearts = """\
 _________ 
|A        |
|# _   _  |
| / ~V~ \ |
| \ Bej / |
|  \ # /  |
|   `.'  #|
|        V|
 ~~~~~~~~~
"""
heartsSymbol = """\
       /\
     .'  `.
    '      `.
 .'          `.
{              }
 ~-...-||-...-~
       ||
      '--`
"""
spades = """\
 _________ 
|A        |
|@   *    |
|   / \   |
|  /_@_\  |
|    !    |
|   ~ ~  @|
|        V|
 ~~~~~~~~~
"""
spadesSymbol = """\
 .-~~~-__-~~~-.
{              }
 `.          .'
   `.      .'
     `.  .'
       \/
"""


menu = 0
balance = 100


while menu != 2:
	print("YOU HAVE ", balance, "SEK IN YOUR ACCOUNT RIGHT NOW\n" + "PRESS 1 TO TRY TO GUESS THE CARD\n" + "PRESS 2 TO TAKE YOUR EARNINGS AND GO\n")
	try:
		menu = int(input("MAKE YOUR CHOICE\n"))
	except:
		print("NOT A NUMBER")
	if (menu == 1 and (balance - 50) >= 0):
		balance = balance - 50
		color = random.randint(1, 4)
		print("THE MACHINE HAS RANDOMED A COLOR\n", "PRESS 1 IF YOU THINK THE COLOR IS CLUBS\n", "PRESS 2 IF YOU THINK THE COLOR IS DIAMONDS\n", "PRESS 3 IF YOU THINK THE COLOR IS HEARTS\n", "PRESS 4 IF YOU THINK THE COLOR IS SPADES\n")
		choosenColor = int(input())
		if choosenColor == color:
			print("CONGRATULATIONS\n" + "YOU HAVE CHOOSEN THE RIGHT CARD")
			balance = balance + 150
		else:
			if color == 1:
				print(clubsSymbol, "\nWRONG COLOR", "\nTHE CORRECT COLOR WAS CLUBS")
			elif color == 2:
				print(diamondsSymbol, "\nWRONG COLOR", "\nTHE CORRECT COLOR WAS DIAMONDS")
			elif color == 3:
				print(heartsSymbol, "\nWRONG COLOR", "\nTHE CORRECT COLOR WAS HEARTS")
			elif color == 4:
				print(spadesSymbol, "\nWRONG COLOR", "\nTHE CORRECT COLOR WAS SPADES")
	elif (menu == 1 and (balance - 50) < 0):
		print("YOU DON'T HAVE ENOUGH MONEY")
	elif (menu == 2 and balance > 0):
		print("YOUR MONEY WILL NOW BE PAYED OUT TO YOUR ACCOUNT\n", "YOU NOW HAVE ", balance, " IN YOUR ACCOUNT\n", "GOODBYE")
	elif (menu == 2 and balance == 0):
		print("HAHA YOU'RE BROKE")

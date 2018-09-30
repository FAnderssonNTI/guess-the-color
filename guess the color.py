import random

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
    if menu == 1:
        color = random.randint(1, 4)
        print("THE MACHINE HAS RANDOMED A COLOR\n" + "PRESS 1 IF YOU THINK THE COLOR IS CLUBS\n" + "PRESS 2 IF YOU THINK THE COLOR IS DIAMONDS\n" + "PRESS 3 IF YOU THINK THE COLOR IS HEARTS\n" + "PRESS 4 IF YOU THINK THE COLOR IS SPADES\n")
    elif menu == 2:
        print("YOUR MONEY WILL NOW BE PAYED OUT TO YOUR ACCOUNT\n" + "GOODBYE")

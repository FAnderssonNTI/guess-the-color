import random

color = random.randint(1, 4)

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



print(clubs)
print(diamonds)
print(hearts)
print(spades)
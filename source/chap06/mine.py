import random

board= [[False for x in range (10)] for y in range(10)]

for r in range(10):
    for c in range(10):
        if( random.random() < 0.3 ):
            board[r][c] = True

for r  in range(10): 
    for c in range(10): 
        if board[r][c] :
            print("# ", end="")
        else:
            print(". ", end="")
    print()

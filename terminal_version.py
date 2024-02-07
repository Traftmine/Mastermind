import random as rm

COLORS = {1:'RED',2: 'BLUE', 3:'GREEN', 4:'YELLOW'}

def game_start():
    game = []
    for i in range(1,len(COLORS)+1):
        game.append(rm.randint(1,4))
    return game

def main():
    game = game_start()
    print(game)
    Not_correct = True
    guesses = [False for i in range(4)]
    while(Not_correct):
        guess = list(map(int,(input("Your guess : ")).split(' ')))
        i = 0
        for e in guess:
            if e == game[i]:
                guesses[i] = True
            else:
                guesses[i] = False
            i+=1
        true_count = guesses.count(True)
        if true_count == 4:
            Not_correct = False
            print("Well Done !!")
        else:
            print(guesses)
    return 0

main()
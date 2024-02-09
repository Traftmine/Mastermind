import random as rm

COLORS = {1:'RED',2: 'BLUE', 3:'GREEN', 4:'YELLOW'}

def game_start():
    game = []
    for i in range(1,len(COLORS)+1):
        game.append(rm.randint(1,5))
    return game

def solution(game):
    print("Here is the solution : " + str(game))

def main():
    game = game_start()
    Not_correct = True
    guesses = [False for i in range(4)]
    guesses_for_user = ["" for i in range(4)]
    while(Not_correct):
        guess = list(map(int,(input("Your guess : ")).split(' ')))
        if guess == [0, 0, 0, 0]:
            solution(game)
            return 0
        i = 0
        for e in guess:
            if e == game[i]:
                guesses[i] = True
                guesses_for_user[i] = "Well Placed"
            else:
                if e in game:
                    guesses_for_user[i] = "Wrongly Placed"
                else:
                    guesses_for_user[i] = "Not in"
                guesses[i] = False
            i+=1
        true_count = guesses.count(True)
        if true_count == 4:
            Not_correct = False
            print("Well Done !!")
        else:
            print(guesses_for_user)
    return 0

main()
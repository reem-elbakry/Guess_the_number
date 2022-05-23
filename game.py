#!/usr/bin/env python3    
#interpreter... to execute our script


import random
number = random.randrange(1,100,5)

trials = 10
lose = 0
win = 0

while(trials>0):

    file = open('player.txt', 'r')
    games = file.read()

    games = games.split()
    times = len(games)
    win = games.count('winner!')
    lose = games.count('loser!')

    file.close()
    if trials == 10:
        print("Hello ya player!:D")
        print("you played", times, "times")
        print("you win ", win)
        print("you lose ", lose)

        print("<<<<<<<<lets play>>>>>>>>>")

    guess = input("guess the number: ")
    guess = int(guess)

    if guess > number:
        print("Random number is less than your guess, try again!")
    elif guess < number:
        print("Random number is large than your guess, try again!")
    else:
        print("you won!")

        player = open('player.txt', 'a')
        player.write("winner! ")
        player.close()

        number = random.randrange(1,100,5)
        continue                        #if won in trial 7...has 3 trials 
    trials -= 1
    if trials == 0:
        print("game over!")
        player = open('player.txt', 'a')
        player.write("loser! ")
        player.close()
        play = input("play again?")
        print("<<<<<<<<<<<>>>>>>>>>>>")
        if play == "yes":
            trials = 10
        else:
            print("bye!")






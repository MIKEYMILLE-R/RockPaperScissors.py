# resubmission with fixed final score
# and reflect player

import random
import time


moves = ['rock', 'paper', 'scissors']


# Ensures typos don't crash the game
def valid_input(prompt, options):
    while True:
        option = input(prompt).lower()
        if option in options:
            return option


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


# Player is parent class and also "rock" player
class Player:
    # The score that will increment
    # after each round
    def __init__(self):
        self.score = 0

    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        self.my_move = None
        self.their_move = None



# Lets you input your move
class HumanPlayer(Player):
    def move(self):
        move = valid_input("Choose: 'Rock' 'Paper' or 'Scissors'\n",
                           ['rock', 'paper', 'scissors'])
        return move


# Random player
class RandomPlayer(Player):
    def move(self):
        return(random.choice(moves))


# Reflect player
class ReflectPlayer(Player):
    def __init__(self):
        super().__init__()
        self.my_move = None
        self.their_move = None
    
    def learn(self, my_move, their_move):
        self.their_move = their_move

    def move(self):
        while True:
            if self.their_move is None:
                return "rock"
            else:
                return self.their_move

# Cycle Player
class CyclePlayer(Player):
    def __init__(self):
        super().__init__()
        
        self.m = 0
    
    def move(self):
        if self.m % 3 == 0:
            self.m +=1 
            return 'rock'
        if self.m % 3 == 1:
            self.m +=1 
            return 'paper'
        if self.m % 3 == 2:
            self.m +=1
            return 'scissors'


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def play_round(self):
        # Creates two players that choose moves
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1} Player 2: {move2}")
        if beats(move2, move1):
            print("you lost...")
            self.p2.score += 1
        if beats(move1, move2):
            print("you win!!!")
            self.p1.score += 1
        else:
            print("it's a tie...")
        time.sleep(1)
        print(f"Player1: {self.p1.score}"
              f"  Player2: {self.p2.score}")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)


# Adjust rounds played by changing
# the number in the for loop
    def play_game(self):
        print("\nWhichever player has more points at the "
              "end of three rounds wins!")
        for match in range(1, 4):
            self.play_round()
            time.sleep(2)
        if self.p1.score > self.p2.score:
            print("\nYOU WON!!")
        else:
            print("\nYou lost...")
        print(f"Player1: {self.p1.score}"
              f"  Player2: {self.p2.score}")
        print("Game over!")


# Change the computer player here  VVV
if __name__ == '__main__':
    game = Game(HumanPlayer(), RandomPlayer())
    game.play_game()

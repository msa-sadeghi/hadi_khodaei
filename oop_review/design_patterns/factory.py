from abc import ABC, abstractmethod
from random import choice
class Base(ABC):
    choices = ['r', 'p', 's']
    @abstractmethod
    def take_action(self):
        pass
class Human(Base):
    def take_action(self):
        user_choice = input("enter your choice (r, p, s): ")
        return user_choice
    
class Computer(Base):
    def take_action(self):
        return choice(self.choices)
class Game:
    def start_game():
        game_type = input('please choose game type("s" for single "m" for multiple): ')
        if game_type == "s":
            p1 = Human()
            p2 = Computer()
        elif game_type == "m":
            p1 = Human()
            p2 = Human()
        else:
            print("Invalid input")
            p1 = None
            p2 = None
        return p1, p2
    
if __name__ == "__main__":
    player1 , player2 = Game.start_game()
    for player in [player1, player2]:
        player.take_action()
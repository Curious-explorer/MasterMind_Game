"""
    CS5001
    Spring 2022
    Pratik Patil
    Project MasterMind Game
    
    mastermind_game -
    This file contains main function of the mastermind game. It initializes the game.
"""

# Importing Libraries
import turtle
from MasterMind import MasterMind
from Constants import *

def main():
    """
         Main funtion -
            parameters - none 

            return - none

            working - This is the main function for mastermind game.
    """
    # Initialising the class
    m1 = MasterMind(COLORS)
    # Starting the game
    m1.initialize()
    turtle.mainloop()

if __name__ == '__main__':
    main()

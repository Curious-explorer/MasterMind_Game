"""
    CS5001
    Spring 2022
    Pratik Patil
    Project MasterMind Game
    
    mastermind class -
    This file contains major class which runs the game. It needs external initialization to get started.
"""

# Importing Libraries
import turtle
from Marble import *
import random
from datetime import datetime
from DrawingClass import *


class MasterMind:
    def __init__(self, colors):
        """
            MasterMind Class Constructor -
            parameters -
                colors - list of colors, which are given as option to user

            return - none

            working - This function initializes the instance variable
        """
        self.colors = colors

    def write_names(self):
        """
            write_names method -
            parameters - none

            return - none

            working - This method will write name of the game at top position on screen
        """
        turtle.goto(0, 350)
        turtle.write("MasterMind!", align='center', font=('American Typewriter', 28))
        
    def initiate_pointer(self):
        """
            initiate_pointer method -
            parameters - none

            return - none

            working - This method initializes the pointer which helps user to know which number of guess they are on.
        """
        # Creating new turtle and setting it's properties
        self.pointer = turtle.Turtle()
        self.pointer.hideturtle()
        self.pointer.speed(0)
        self.pointer_x = -330
        self.pointer_y = 315
        self.pointer.penup()
        # Changing shape of the turtle
        self.pointer.shapesize(2,3,1)
        self.pointer.color('black', 'red')
        # Moving turtle to start position of pointer, i.e. first guess
        self.pointer.goto(self.pointer_x, self.pointer_y)
        self.pointer.showturtle()

    def ask_name(self):
        """
            ask_name method -
            parameters - none

            return - none

            working - This ask user's name in popup at the start of the game.
        """
        # Start message
        self.player_name = turtle.textinput('Welcome!!', 'Please enter your name :)')
        # Repeated message if user does not gives any input
        while len(self.player_name.strip()) == 0:
            self.player_name = turtle.textinput('Welcome!!', 'Please enter valid name :)')
        
    
    def initialize(self, x=0,y=0):
        """
            initialize method -
            parameters - x - x coordinate of mouse click
                        y - y coordinate of mouse click

            return - none

            working - This method initializes the game layout and buttons, also it initializes most of the instance variables.
        """
        # Checking if initialization is done at the start or later in the game
        # If it is done later in the game then x and y coordinates will have values of mouse click
        if x == 0 and y == 0:
            self.get_screen()
            self.ask_name()
        else:
            turtle.clearscreen()
        # Initializing turtle and setting it's properties
        self.turtle = turtle.getturtle()
        self.turtle.penup()
        self.turtle.hideturtle()
        self.turtle.speed(0)
        # Initiating instance variables and screen settings
        self.write_names()
        self.generate_code()
        self.row = 1
        self.column = 1
        self.erased_colors = []
        self.turtle.penup()

        # Initiating game layout
        self.drawing_class = DrawingClass(self.turtle, self.colors)
        self.drawing_class.draw_rectangle(370, 500, {'x': 0,'y': 340}, 'black', 5)
        self.drawing_class.draw_rectangle(350, 500, {'x': 360,'y': 340}, 'blue', 5)
        self.drawing_class.draw_rectangle(730, 150, {'x': 360,'y': -170}, 'grey', 5)
        self.drawing_class.draw_grid({'x': -370,'y': 290}, 50, 370, 'black', 5)

        # Initiating game layout and collecting returned dictionaries in variables
        self.marble_objects = self.drawing_class.draw_marble_array({'x': -350,'y': 350})
        self.choices_dict  = self.drawing_class.draw_6_choices({'x': -30,'y': -250})
        self.peg_dict = self.drawing_class.draw_pegs_array({'x': -50,'y': 360})

        # Initialising buttons
        self.check_turtle = self.add_button('checkbutton.gif', 20, -230)
        self.xbutton_turtle = self.add_button('xbutton.gif', 100, -230)
        self.quit_turtle = self.add_button('quit.gif', 230, -230, self.close_game)

        # Initializing pointer
        self.initiate_pointer()

        # writing leaderboard on screen
        self.write_leaderboard('leaderboard.txt')

        # Ready to receive mouse input
        self.screen.onclick(self.shift_color)
        

    def write_leaderboard(self, file_path):
        """
            write_leaderboard method -
            parameters - file_path - path of leaderboard.txt file

            return - none

            working - This read leaderboard.txt file and write the top 10 leaders onto the screen.
                    It will also initiate error message if the file is not found in storage.
        """
        # Setting leaderboard title position and writing leaderboard title
        leaderboard_x = 100
        leaderboard_y = 315
        self.turtle.goto( leaderboard_x, leaderboard_y)
        self.turtle.color('blue')
        turtle.write("Leaderboard (Top 10)", align='left', font=('American Typewriter', 18))

        # Trying to open leaderboard.txt file and raising error if not found
        try:
            with open('leaderboard.txt', mode = 'r') as leaderboard:
                lines = leaderboard.readlines()
        except Exception as e:
            # Initiating error message and logging error in error log file
            self.leader_board_not_found()
            now = datetime.now()
            dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
            dt_list = dt_string.split()
            with open("mastermind_errors.err", mode = 'a') as error_log:
                error_log.writelines(f"date(dd/mm/yyyy) => {dt_list[0]}, time => {dt_list[1]}, error => {e} \n")

            # Creating new leaderboard.txt file
            with open('leaderboard.txt', mode = 'w') as leaderboard:
                lines = []

        # storing players info in form of dictionary
        self.players_info = dict()
        for i in lines:
            a, b = i.split(':')
            self.players_info[a.strip(),b.strip()] = int(b.strip())
        # Sorting keys of dictionary info based on number of guesses
        players_sorted = sorted(self.players_info, key=self.players_info.get)

        # looping through sorted keys and printing names of leaders on leaderboard
        leaderboard_x = 50
        for i in players_sorted[:10]:
            leaderboard_y -= 30
            turtle.goto(leaderboard_x, leaderboard_y)
            turtle.write(f"{i[0]} : {self.players_info[i]}", align='left', font=('American Typewriter', 18))

    def add_button(self, name, x_pos, y_pos, trigger = False): # Might need to remove trigger here
        """
            add_button method -
            parameters - name - name of shape gif
                        x_pos - x coordinate of button position
                        y_pos - y coordinate of button position
                        trigger - method to be used for onclick function

            return - t2 - turtle assigned with the button

            working - This method creates button and assigns seperate turtle to new button
        """
        # Initializing turtle and setting it's parameters
        t2 = turtle.Turtle()
        t2.speed(0)
        t2.penup()
        # Going to initial button position
        t2.goto(x_pos, y_pos)
        self.screen.addshape(name)
        t2.shape(name)
        # Adding onclick function if given and returning the turtle
        if trigger:
            t2.onclick(trigger)
        return t2

    def leader_board_not_found(self):
        """
            leader_board_not_found method -
            parameters - none

            return - none

            working - This method will show leaderboard not found message.
        """
        # Showing lose message and setting onclick function
        self.screen.addshape('leaderboard_error.gif')
        self.leaderboard_msg = turtle.Turtle()
        self.leaderboard_msg.shape('leaderboard_error.gif')
        self.leaderboard_msg.onclick(self.hide_learderboard_msg)

    def hide_learderboard_msg(self, x=0, y=0):
        """
            hide_learderboard_msg method -
            parameters -x - x coordinate of mouse click
                        y - y coordinate of mouse click

            return - none

            working - This method will hide leaderboard not found message once clicked on it.
        """
        self.leaderboard_msg.hideturtle()

    def close_game(self, x, y):
        """
            close_game method -
            parameters -x - x coordinate of mouse click
                        y - y coordinate of mouse click

            return - none

            working - This method will show quit message, and once clicked on the screen it will close the game.
        """
        # Showing lose message and setting onclick function
        self.screen.addshape('quitmsg.gif')
        t = turtle.Turtle()
        t.shape('quitmsg.gif')
        self.screen.exitonclick()

    def reset_guess(self, x =0, y=0):
        """
            reset_guess method -
            parameters -x - x coordinate of mouse click
                        y - y coordinate of mouse click

            return - none

            working - This method will reset the current guess and also initiate reset of current choice marbles
        """
        # Resetting current guess in marble array
        for i in range(1, self.column):
            self.marble_objects[self.row, i].erase()
            self.marble_objects[self.row, i].draw_empty()
        # initiating reset of choice marbles
        self.reset_choices()

    def reset_choices(self, x =0, y=0):
        """
            reset_choices method -
            parameters -x - x coordinate of mouse click
                        y - y coordinate of mouse click

            return - none

            working - This method will reset the 6 choice colors
        """
        # Reseting column and erased color list
        self.erased_colors = []
        self.column = 1
        # looping thorugh current choice dictionary to reseting colors which are erased
        for key, value in self.choices_dict.items():
            if value.is_empty:
                value.erase()
                value.draw()
        # Getting ready for next response
        self.screen.onclick(self.shift_color)
    
    def check_guess(self, x =0, y=0, flag = True):
        """
            check_guess method -
            parameters - x - x coordinate of mouse click
                        y - y coordinate of mouse click
                        flag - to know if this method is running while game or called seperately for testing

            return - none

            working - This method will check the guess against secret code
        """
        # looping through erased colors
        if len(self.erased_colors) == 4:
            self.cows = 0
            self.bulls = 0
            # Checking for cows and bulls based on color and position
            for enum, color in enumerate(self.code):
                if color in self.erased_colors:
                    if self.erased_colors[enum] == color:
                        self.bulls += 1
                    else:
                        self.cows += 1
            # If the method is used during game then displaying pegs for current guess
            if flag:
                self.show_pegs()
    

    def show_pegs(self):
        """
            show_pegs method -
            parameters - none

            return - none

            working - This function will show bulls and cows based on the current guess checking status 
        """
        # Creating counter to see number of bulls
        self.counter = 0
        # looping through bulls and cows to show output in random format
        for i in range(1, 5):
            if self.cows > 0 or self.bulls > 0:
                self.peg_dict[self.row, i].erase()
                if self.bulls > 0:
                    self.peg_dict[self.row, i].set_color('black')
                    self.bulls -= 1
                    self.counter += 1
                    self.peg_dict[self.row, i].draw()
                elif self.cows > 0:
                    self.peg_dict[self.row, i].set_color('red')
                    self.cows -= 1
                    self.peg_dict[self.row, i].draw()
        # If all guess are bulls then displaying winner message
        if self.counter == 4:
            self.won_game('leaderboard.txt')
        # If all guess are used then displaying lose message
        if self.row == 10:
            self.lose_game()
        # changing pointer position and reseting choice colors
        # Also updating current row and column values
        self.screen.onclick(self.shift_color)
        self.row += 1
        self.pointer_y -= 50
        self.pointer.goto(self.pointer_x, self.pointer_y)
        self.reset_choices()

    def won_game(self, file_path):
        """
            won_game method -
            parameters - file_path - file path for leaderboard file

            return - none

            working - This method will show winner message, and once clicked on the message it will restart the game.
                Also this method will save top 10 people in leaderboard.txt file.
        """
        # Collecting current player infor in players_info instance variable dictionary
        self.players_info[self.player_name,self.row] = self.row
        # Sorting keys based on values, i.e. number of guesses taken
        player_sorted = sorted(self.players_info, key=self.players_info.get)
        # looping through sorted keys to save top 10 players in leaderboard.txt
        with open(file_path, mode= 'w') as leaderboard:
            for i in player_sorted[:10]:
                leaderboard.writelines(f"{i[0]} : {i[1]}\n")
        # Showing winner message and setting onclick function
        self.screen.addshape('winner.gif')
        t = turtle.Turtle()
        t.shape('winner.gif')
        t.onclick(self.initialize)

    def lose_game(self):
        """
            lose_game method -
            parameters - none

            return - none

            working - This method will show lose message, and once clicked on the message it will restart the game.
        """
        # Showing lose message and setting onclick function
        self.screen.addshape('Lose.gif')
        t = turtle.Turtle()
        t.shape('Lose.gif')
        t.onclick(self.initialize)
    
    def generate_code(self):
        """
            generate_code method -
            parameters - none

            return - none

            working - This method generates a secret code using random.sample method
        """
        self.code = random.sample(self.colors, 4)
    
    def shift_color(self, x, y):
        """
            shift_color method -
            parameters -
                x - x coordinate of mouse click
                y - y coordinate of mouse click

            return - none

            working - This method finds which color choice marble is clicked and then assigns that color to
                correspoinding marble in marble array, also it initiates the method which checks the guess.
        """
        # Resetting the choices if x button is clicked
        self.xbutton_turtle.onclick(self.reset_guess)
        # Looping through choices array to find clicked color
        for key, value in self.choices_dict.items():
            # Changing row in marbles to write next guess
            if self.column == 5:
                break
            # Checking which color is clicked and whether it is being clicked twice
            elif value.clicked_in_region(x, y) and value.color not in self.erased_colors:
                # erasing clicked choice marble
                value.erase()
                value.draw_empty()
                # Setting erased color as instance variable
                self.color = value.color
                # Filling marble in marble array for guess
                self.marble_objects[self.row, self.column].erase()
                self.marble_objects[self.row, self.column].color = self.color
                self.marble_objects[self.row, self.column].draw()
                # Adding color of choice in erased colors list
                self.erased_colors.append(self.color)
                # incrementing columns they vary from 1 to 4
                self.column += 1
                if self.column == 5:
                    # Checking if 4 colors are choosen as guess and checkbutton is clicked
                    self.check_turtle.onclick(self.check_guess)

    def get_screen(self):
        """
            get_screen method -
            parameters -none

            return - none

            working - This method opens the screen using turtle library, using game settings
        """
        # Opening Screen
        self.screen = turtle.getscreen()
        # Setting up screen size and screen title
        self.screen.setup(SCREEN_WIDTH, SCREEN_LENGTH)
        self.screen.title(SCREEN_TITLE)

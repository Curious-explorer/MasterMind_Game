"""
    CS5001
    Spring 2022
    Pratik Patil
    Project MasterMind Game
    
    Drawing Class -
    This Class is used to draw game layout, it uses Marble class to draw marbles.
"""

# Importing Libraries
import turtle
from Marble import *
from Constants import *


class DrawingClass:
    def __init__(self, turtle, colors):
        """
            DrawingClass Constructor -
            parameters -
                turtle - turtle which will be used to draw the shapes
                colors - list of colors, which are given as option to user

            return - none

            working - This function initializes the instance variables
        """
        self.turtle = turtle
        self.colors = colors

    def draw_rectangle(self, length, width, corner_coors, border_color = 'black', pensize = 1):
        """
            draw_rectangle method -
            parameters -
                length - length of the rectangle to be drawn
                width - width of the rectangle to be drawn
                corner_coors - top right corner coordinates of square
                border_color - color used for rectangle border
                pensize - pensize used to draw rectangle

            return - none

            working - This method will draw rectangle as mentioned by parameters
        """
        # Setting bordercolor and pensize
        self.turtle.color(border_color)
        self.turtle.pensize(pensize)
        # Going to top right corner position and putting pen down
        self.turtle.goto(corner_coors['x'], corner_coors['y'])
        self.turtle.pendown()

        # Looping twice to draw the rectangle
        for i in [1, 2]:
            self.turtle.right(RIGHT_ANGLE)
            self.turtle.forward(width)
            self.turtle.right(RIGHT_ANGLE)
            self.turtle.forward(length)

        # Changing turtle settings to default
        self.defalt_settings()

    def draw_grid(self, start_point, row_height, length, border_color = 'black', pensize = 1):
        """
            draw_grid method -
            parameters -
                start_point - start position to draw lines grid,
                        this is left most point of top line in grid
                row_height - gap to keep between two lines
                length - length of line
                border_color - color for the grid lines
                pensize - pen size for the grid lines

            return - none

            working - This method draws multiple grid lines, which help user
                identify the exact pegs for current guess.
        """
        # Setting bordercolor and pensize
        self.turtle.color(border_color)
        self.turtle.pensize(pensize)
        # Going to the start position and putting pen down
        self.turtle.goto(start_point['x'], start_point['y'])
        self.turtle.pendown()
        # Looping to draw 10 grid lines
        for i in range(0, 9):
            self.turtle.forward(length)
            self.turtle.penup()
            self.turtle.backward(length)
            self.turtle.right(RIGHT_ANGLE)
            self.turtle.forward(row_height)
            self.turtle.left(RIGHT_ANGLE)
            self.turtle.pendown()
        # Changing turtle settings to default
        self.defalt_settings()

    def draw_marble_array(self, start_point):
        """
            draw_marble_array method -
            parameters -
                start_point - position from which marble array has to be drawn, here
                            it is the position for top left marble's start point

            return - marble_objects - dictionary containing tuples as keys, which are row and column number in array
                            and object's memory address as values.

            working - This method draws the marble array and return a dictionary containing objects to use later.
        """
        marble_objects = dict()
        # Looping in order to draw marble array of 10 rows and 4 columns
        for i in range (1, 11):
            for j in range(1, 5):
                # Creating marble objects
                marble = Marble(Point(start_point['x'] + j*50, start_point['y'] - i*50), "blue")
                marble.draw_empty()  # Drawing empty marble
                # Storing marble object's memory address
                marble_objects[i, j] = marble
        # Changing setting to default
        self.defalt_settings()
        # Returning marble object dictionary
        return marble_objects


    def draw_pegs_array(self, start_point):
        """
            draw_pegs_array method -
            parameters -
                start_point - startpoint from where the pegs will be drawn, here it is
                            center point of first group of pegs

            return - peg_dict - dictionary containing peg (small marble) memory address as values
                        and row number and group position number as tuple for key

            working - This method draws the pegs array and return a dictionary containing objects to use later.
        """
        peg_dict = dict()
        # Looping 10 times to draw 10 groups of 4 pegs
        for i in range (1, 11):
            # Start positions
            x = start_point['x']
            y = start_point['y'] -i*50
            distance = 10
            # Variables to manipulate nested for loop to draw 4 pegs
            a = -1
            b = 1
            for j in range(1, 5):
                marble = Marble(Point(x + a * distance, y + b * distance), "blue", 5)
                peg_dict[i, j] = marble
                marble.draw_empty()
                # Changing  variable values to get all 4 combinations
                if j % 2 == 0:
                    a = -1
                    b = -1
                else:
                    a = 1
        # Changing setting to default
        self.defalt_settings()
        # Returning peg object dictionary
        return peg_dict

    def draw_6_choices(self, start_point):
        """
            draw_6_choices method -
            parameters -
                start_point - here it is the start position which start position to draw right most marble

            return - choices_dict - dictionary containing memory address of 6 choice marbles and
                                    their start coordinates as key in tuple form

            working - This method draws the choice marble array and return a dictionary containing objects to use later.
        """
        choices_dict = dict()
        # Looping 6 times to draw all the choices given to user
        for i in range(1,7):
            # Drawing marble using marble class and at uniform distance
            marble = Marble(Point(start_point['x'] - i*50, start_point['y']), self.colors[i-1]) 
            marble.draw()
            # Storing object's memory address
            choices_dict[start_point['x'] - i*50, start_point['y']] = marble
        # Changing setting to default
        self.defalt_settings()
        # Returning choice marble object dictionary
        return choices_dict

    def defalt_settings(self):
        """
            defalt_settings method -
            parameters - none

            return - none

            working - This method resets the turtle setting to default ones
                For this program default settings are border color - black,
                pensize = 1, and pen position up.
        """
        self.turtle.penup()
        self.turtle.color('black')
        self.turtle.pensize(1)

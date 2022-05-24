MasterMindGame Program Design ->

I used Object Oriented Design while coding this project. My plan was to divide problem into small pieces and
then automate those pieces using methods of class. I am successful in creating the game using this approach.
To keep the learning curve short, I tried to keep the names as explainatory as possible.
Also I have written comments at all the necessary places.

I was able to logically divide the game into small steps, which I was able to write as code.
Because of OOD, writing code was easy. And I could use methods to do link the tasks.
I made one major class for gameplay (MasterMind Class), where most of the working happens. But for one time tasks like drawing
the layout I have created a different class (DrawingClass).

The program will raise error if leaderboard file is not found, but it will recreate it as soon as you click on the error.

The program will share lose message if player is unable to guess the code in 10 guesses. If he can then
program will show winner message.
Constants are saved in different file to get better view.

What are the rules of the game?
The game has simple rules -
1. Try guessing 4 color code, you guess will be pointed by the red arrow
2. If you get a red peg (peg - small circle besides big ones) that means one your color is correct,
but it is at wrong position
3. If you get a black peg that means one your color is correct, and it's position is also correct.
4. You have to try till you get all 4 black pegs!

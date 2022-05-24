"""
    CS5001
    Spring 2022
    Pratik Patil
    Project MasterMind Game
    
    Test for mastermind game -
    This code will test all the functions in mastermind class which do not include turtle class.
"""

# Importing libraries
import unittest
from MasterMind import MasterMind
from Constants import *


class TestMasterMind(unittest.TestCase):
    def test_generate_code(self):
        """
            test_generate_code method -
            parameters - none

            return - none

            working - This method will test the secret code, it's length and whether it has 4 distinct values or not.
        """
        # Creating object of mastermind class
        m1 = MasterMind(COLORS)
        # Generating code
        m1.generate_code()
        # Checking if the secret code has 4 elements
        self.assertEqual(len(m1.code), 4)
        # Checking for distinct 4 choices
        self.assertEqual(len(set(m1.code)), len(m1.code))


    def test_check_guess(self):
        """
            test_check_guess method -
            parameters - none

            return - none

            working - This method will test the checking method in mastermind class.
        """
        # Creating object of mastermind class
        m1 = MasterMind(COLORS)
        # Setting secret code
        m1.code = ["red", "blue", "green", "yellow"]

        #First test->
        # Here comparing guess with secret code and expecting results
        code1 = ["red", "blue", "green", "yellow"]
        code1_ans = {'bulls' : 4, 'cows' : 0}
        m1.erased_colors = code1
        m1.check_guess(x =0, y=0, flag = False)
        self.assertEqual(code1_ans['bulls'], m1.bulls)
        self.assertEqual(code1_ans['cows'], m1.cows)

        #Second test->
        code2 = ["green", "yellow", "purple", "black"]
        code2_ans = {'bulls' : 0, 'cows' : 2}
        m1.erased_colors = code2
        m1.check_guess(x =0, y=0, flag = False)
        self.assertEqual(code2_ans['bulls'], m1.bulls)
        self.assertEqual(code2_ans['cows'], m1.cows)

        #Third test->
        code3 = ["blue", "green", "yellow", "purple"]
        code3_ans = {'bulls' : 0, 'cows' : 3}
        m1.erased_colors = code3
        m1.check_guess(x =0, y=0, flag = False)
        self.assertEqual(code3_ans['bulls'], m1.bulls)
        self.assertEqual(code3_ans['cows'], m1.cows)

        #Fourth Test->
        code4 = ["red", "blue", "purple", "black"]
        code4_ans = {'bulls' : 2, 'cows' : 0}
        m1.erased_colors = code4
        m1.check_guess(x =0, y=0, flag = False)
        self.assertEqual(code4_ans['bulls'], m1.bulls)
        self.assertEqual(code4_ans['cows'], m1.cows)
        
        #Fifth Test->
        code5 = ["blue", "green", "yellow", "red"]
        code5_ans = {'bulls' : 0, 'cows' : 4}
        m1.erased_colors = code5
        m1.check_guess(x =0, y=0, flag = False)
        self.assertEqual(code5_ans['bulls'], m1.bulls)
        self.assertEqual(code5_ans['cows'], m1.cows)
    
def main():
    unittest.main(verbosity=3)

if __name__ == "__main__":
    main()

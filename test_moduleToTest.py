# This module contains tests for module "moduleToTest.py"

# Libraries and modules
import unittest # Module for test clesses
import moduleToTest # Module to be tested

#Test clesses 

class ClueTest(unittest.TestCase):
    
    def test_update_clue(self):
        clue = list("?????")
        secret_word = "sorsa"
        guessed_word = "sorsa"
        moduleToTest.update_clue(guessed_word,secret_word,clue)
        expected_result = list(guessed_word)
        result = clue
        self.assertEqual(result, expected_result)

if __name__ == "__main__":
    unittest.main()


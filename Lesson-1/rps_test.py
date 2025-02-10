import unittest
from unittest.mock import patch
import random
from rps_minus_one import comp_hands, player_hands, minus_one, determine_winner, print_score, print_hands

class TestGameFunctions(unittest.TestCase):

    def test_comp_hands(self):
        options = ["rock", "paper", "scissors"]
        with patch("random.randint", side_effect=[0, 1]):
            self.assertEqual(comp_hands(options), ("rock", "paper"))

    @patch("builtins.input", side_effect=["1", "3"])
    def test_player_hands(self, mock_input):
        options = ["rock", "paper", "scissors"]
        self.assertEqual(player_hands(options), ("rock", "scissors"))

    @patch("builtins.input", side_effect=["1"])
    @patch("random.randint", return_value=1)
    def test_minus_one(self, mock_rand, mock_input):
        player_hand = ("rock", "scissors")
        computer_hand = ("paper", "rock")
        self.assertEqual(minus_one(player_hand, computer_hand), ("rock", "rock"))

    def test_determine_winner_tie(self):
        scores = [0, 0]
        final_hands = ("rock", "rock")
        self.assertEqual(determine_winner(final_hands, scores), [0, 0])

    def test_determine_winner_player_wins(self):
        scores = [0, 0]
        final_hands = ("rock", "scissors")
        self.assertEqual(determine_winner(final_hands, scores), [1, 0])

    def test_determine_winner_computer_wins(self):
        scores = [0, 0]
        final_hands = ("scissors", "rock")
        self.assertEqual(determine_winner(final_hands, scores), [0, 1])

    def test_print_score(self):
        scores = [2, 1]
        with patch("builtins.print") as mock_print:
            print_score(scores)
            mock_print.assert_called_with("The player has a score of 2 and the computer has a score of 1")
    
    def test_print_hands(self):
        hand_one = ["rock","paper"]
        hand_two = ["paper","scissors"]
        print_hands(hand_one,hand_two)
        
    def test_print_hands_final_hand(self):
        hand = ("paper","rock")
        print_hands(hand)
        hand = ("scissors","rock")
        print_hands(hand)
    
    @patch("builtins.input", side_effect=["1"])
    @patch("random.randint", return_value=1)
    def test_bug(self,mock_rand,mock_input):
        comp = ["rock","rock"]
        player = ["rock","paper"]
        self.assertEqual(minus_one(player,comp),("rock","rock"))
        
        
        
        

if __name__ == "__main__":
    unittest.main()

import unittest
from unittest.mock import patch
import pygame
from toss import update_score, reset_ball, process_game_logic

class TestTossGame(unittest.TestCase):

    def setUp(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        self.ball_x = 400
        self.ball_y = 10
        self.score = 0
        self.balls_remaining = 10
        self.boxes = [(100, 550, 40, 200), (200, 550, 40, 200)]  # Example box positions

    def test_update_score(self):
        """Test score update on hitting a box."""
        hit_box_index = 0  # Simulate hitting the first box
        self.score = update_score(self.score, hit_box_index)
        self.assertEqual(self.score, 1, "Score should increase by the box index plus one")

    def test_reset_ball(self):
        """Test resetting the ball."""
        new_ball_x, new_ball_y = reset_ball()
        self.assertEqual(new_ball_x, 400)
        self.assertEqual(new_ball_y, 10)

    @patch('pygame.event.get')
    def test_process_game_logic(self, mock_get):
        """Test processing of game logic on mouse click."""
        mock_get.return_value = [pygame.event.Event(pygame.MOUSEBUTTONDOWN, {'pos': (400, 300)})]
        # Assuming process_game_logic updates ball_x, ball_y on click
        ball_x, ball_y, ball_moving_horizontally = process_game_logic(self.ball_x, self.ball_y, True)
        self.assertFalse(ball_moving_horizontally, "Ball should stop moving horizontally after a click")

    def tearDown(self):
        pygame.quit()

if __name__ == '__main__':
    unittest.main()

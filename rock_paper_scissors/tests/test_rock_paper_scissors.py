"""Test module for the rock paper scissors game."""
from unittest import mock
import pytest
from rock_paper_scissors.main import rock_paper_scissors


class TestRockPaperScissors:
    """Test suite for the rock paper scissors game against the computer"""

    @mock.patch('random.choice', return_value='rock')
    def test_winning_condition(self, mocked_computer_choice):
        expected_outcome = 'The computer chose: rock\nYou chose: paper\nYou win!'
        assert rock_paper_scissors('paper') == expected_outcome

    @mock.patch('random.choice', return_value='rock')
    def test_losing_condition(self, mocked_computer_choice):
        expected_outcome = 'The computer chose: rock\nYou chose: scissors\nYou lose!'
        assert rock_paper_scissors('scissors') == expected_outcome

    @mock.patch('random.choice', return_value='rock')
    def test_draw(self, mocked_computer_choice):
        expected_outcome = "The computer chose: rock\nYou chose: rock\nIt's a draw!"
        assert rock_paper_scissors('rock') == expected_outcome

    def test_invalid_input_raises_value_error(self):
        with pytest.raises(ValueError):
            rock_paper_scissors('test')

"""
test_moves.py - všechny testy pohybu.

všechny testy pohybu.
"""

from maze_run.draw_maze import parse_grid
from maze_run.moves import move
from maze_run.moves import LEFT, RIGHT, UP, DOWN
from tests.fixtures import level, LEVEL
import pytest

CRATE_MOVES = [
    (LEFT,  (3, 2), (3, 1)),
    (RIGHT, (3, 4), (3, 5)),
    (UP,    (2, 3), (1, 3)),
    (DOWN,  (4, 3), (5, 3)),
]


PATHS = [
    ((UP, LEFT),2, 2),
    ((LEFT, UP), 2, 2),
    ((RIGHT, UP, LEFT, LEFT), 2, 2),
    pytest.param ((DOWN, DOWN), 0, 0, marks=pytest.mark.xfail(reason = 'Záměrná chyba výsledku')),
    ((LEFT, ), 2, 3),
    ((LEFT, RIGHT), 3, 3),
    ((RIGHT, RIGHT), 4, 3),
]

def move_crate(direction, plr_pos, crate_pos):
    """Help function for testing crate moves."""
    #maze = parse_grid(LEVEL)
    move(level, direction)
    assert level[plr_pos[0]][plr_pos[1]] == '*'
    assert level[crate_pos[0]][crate_pos[1]] == 'o'

class TestCrateMoves:
    """All tests crate moves."""

    @pytest.mark.parametrize('direction, plr_pos, crate_pos', CRATE_MOVES)
    def test_move_crate(self, level, direction, plr_pos, crate_pos):
        """After move player and crate moved by one square."""
        print(direction, plr_pos, crate_pos)
        move(level, direction)
        assert level[plr_pos[0]] [plr_pos[1]] == '*'
        assert level[crate_pos[0]][crate_pos[1]] == 'o'

        
    def push_crate_to_wall(self, direction, retezec):
        """Help function to test push to wall."""
        maze = parse_grid(retezec)
        mazepuv = maze
        move(maze, direction)
        assert maze[0] == mazepuv[0]

    def test_push_crate_to_wall_right(self):
        """Test push crate to wall right."""
        plan = """
        #####
        #.*o#
        #####"""
        self.push_crate_to_wall(RIGHT,plan)
        
    def test_push_crate_to_wall_left(self):
        """Test push crate to wall left."""
        plan = """
        #####
        #o*.#
        #####"""
        self.push_crate_to_wall(LEFT,plan)

    def test_push_crate_to_crate(self):
        """Test_push_crate_to_crate."""
        maze = parse_grid('*oo')
        move(maze,RIGHT)
        assert maze ==[['*','o','o']]

    def test_move_crate_to_corner(self, level):
        """Move tom crate to upper left corner."""
        for d in [UP, RIGHT, UP, LEFT, LEFT, LEFT]:
            move(level, d)
        assert level [1][1] == "o"

    def test_move_crate_back_forth(self, level):
        """Sanity check: move the top crate twice."""
        for d in [LEFT, UP, RIGHT, UP, RIGHT, RIGHT, DOWN, LEFT, LEFT, LEFT]:
            move(level, d)
        assert level [2] == list('#o*   #')

class TestPlayerMoves:
    """All tests to move player."""

    @pytest.mark.parametrize('path, expected_x, expected_y', PATHS)
    def test_move_player(self, level, path, expected_x, expected_y):
        """Korektní změna pozice hráče. Více parametrů - path, expected_x, expected_y."""
        for direction in path:
            move(level,direction)
        assert level[expected_y][expected_x] == '*'

    def test_move_to_none(self, level):
        """Direction None generate an Exception."""
        with pytest.raises(TypeError):
            move(level, None)
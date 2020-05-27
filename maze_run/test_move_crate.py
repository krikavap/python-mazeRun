"""
test_move_crate_right.py.

ddd
"""
from maze_run.crate import LEVEL
from maze_run.draw_maze import parse_grid
from maze_run.moves import move
from maze_run.moves import LEFT, RIGHT, UP, DOWN
import pytest

def move_crate(direction, plr_pos, crate_pos):
    """Help function for testing crate moves."""
    maze = parse_grid(LEVEL)
    move(maze, direction)
    assert maze[plr_pos[0]][plr_pos[1]] == '*'
    assert maze[crate_pos[0]][crate_pos[1]] == 'o'

def test_move_crate_left():
    """Test move crate to left."""
    move_crate(LEFT, (3,2), (3,1))

def test_move_crate_right():
    """´Test move crate to right."""
    move_crate(RIGHT, (3,4), (3,5))

def test_move_crate_up():
    """Test move crate to up."""
    move_crate(UP, (2,3), (1,3))

def test_move_crate_down():
    """Test move crate to down."""
    move_crate(DOWN, (4,3), (5,3))

def test_assert_examples():
    """Test some examples."""
    maze = parse_grid(LEVEL)
    assert len(maze) <= 7
    assert 1 < len(maze) < 10
    assert maze[0][0] == '#' and maze[1][1] == '.'
    assert maze[0].count('#') == 7

def push_crate_to_wall(direction, retezec):
    """Help function to test push to wall."""
    maze = parse_grid(retezec)
    mazepuv = maze
    move(maze, direction)
    assert maze[0] == mazepuv[0]

def test_push_crate_to_wall_right():
    """Test push crate to wall right."""
    plan = """
    #####
    #.*o#
    #####"""
    push_crate_to_wall(RIGHT,plan)
    
def test_push_crate_to_wall_left():
    """Test push crate to wall left."""
    plan = """
    #####
    #o*.#
    #####"""
    push_crate_to_wall(LEFT,plan)

def test_push_crate_to_wall_up():
    """Test push crate to wall up."""
    plan = """
    #####
    #.o.#
    #o*.#
    #####"""
    push_crate_to_wall(UP,plan)

def test_push_crate_to_crate():
    """Test_push_crate_to_crate."""
    maze = parse_grid('*oo')
    move(maze,RIGHT)
    assert maze ==[['*','o','o']]

def test_move_to_none():
    """Direction None generate an Exception."""
    maze = parse_grid(LEVEL)
    with pytest.raises(TypeError):
        move(maze, None)

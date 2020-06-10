"""
test_move_crate_right.py.

druhá verze, používá parametrize dat a fixture
"""
from maze_run.draw_maze import parse_grid
from maze_run.moves import move
from maze_run.moves import LEFT, RIGHT, UP, DOWN
import pytest

LEVEL = """
#######
#.....#
#..o..#
#.o*o.#
#..o..#
#.....#
#######"""

LEVEL_NO_DOTS = LEVEL.replace('.', ' ')

PATHS = [
    (UP, LEFT),
    (LEFT, UP),
    (RIGHT, UP, LEFT, LEFT),
    pytest.param((DOWN, DOWN), marks=pytest.mark.xfail(reason = 'záměrná chyba')),
]

PATH_PLAYERPOS = [
    ((LEFT,), 2, 3),
    ((LEFT, RIGHT), 3, 3),
    ((RIGHT, RIGHT), 4, 3),
]

@pytest.fixture(params=[LEVEL, LEVEL_NO_DOTS])
def level(request):
    """Level with four single crates."""
    return parse_grid(request.param)

def test_move_crate_to_corner(level):
    """Move tom crate to upper left corner."""
    for d in [UP, RIGHT, UP, LEFT, LEFT, LEFT]:
        move(level, d)
    assert level [1][1] == "o"

def test_move_crate_back_forth(level):
    """Sanity check: move the top crate twice."""
    for d in [LEFT, UP, RIGHT, UP, RIGHT, RIGHT, DOWN, LEFT, LEFT, LEFT]:
        move(level, d)
    assert level [2] == list('#o*   #')

@pytest.mark.parametrize('path', PATHS)
def test_paths(path, level):
    """Different paths lead to the same spot. Jeden parametr (path)."""
    for direction in path:
        move(level,direction)
    assert level[2][2] == '*'

@pytest.mark.parametrize('path, expected_x, expected_y', PATH_PLAYERPOS)
def test_move_player(level, path, expected_x, expected_y):
    """Korektní změna pozice hráče. Více parametrů - path, expected_x, expected_y."""
    for direction in path:
        move(level,direction)
    assert level[expected_y][expected_x] == '*'


# tyto další testy nevyužívají data připravená formulí fixtures
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

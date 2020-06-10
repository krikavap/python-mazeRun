"""
fixture.py - úvodní data.

obsahuje úvodní data pro testy.
"""

import pytest
from maze_run.draw_maze import parse_grid

LEVEL = """
#######
#.....#
#..o..#
#.o*o.#
#..o..#
#.....#
#######"""

LEVEL_NO_DOTS = LEVEL.replace('.', ' ')
@pytest.fixture(params=[LEVEL, LEVEL_NO_DOTS])
def level(request):
    """Level with four single crates."""
    return parse_grid(request.param)
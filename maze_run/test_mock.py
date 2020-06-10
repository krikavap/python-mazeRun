"""
test_mock.py. 

test_mock.py.
"""
from pygame import image, Rect
import pygame

pygame.init()
pygame.display.set_mode((800, 600))
relpath = 'maze_run/'
relpath_images = 'maze_run/images/'

def draw(surface):
    """Draw."""
    img = image.load(relpath_images+'tiles.xpm')
    surface.blit(img, Rect((0, 0, 32, 32)), Rect((0, 0, 32, 32)))
    pygame.display.update()



from unittest import mock

@mock.patch('pygame.display.update')
def test_mocking(mock_update):
    """Mock."""
    display = pygame.display.get_surface()
    draw(display)
    assert mock_update.called is True
    assert mock_update.call_count == 1

def test_blit():
    """Blit."""
    mock_disp = mock.MagicMock(name='display')
    draw(mock_disp)
    assert mock_disp.blit.called is True

def test_bad_mocks():
    """Bad mocks."""
    mo = mock.MagicMock()
    assert mo.twenty_blue_dolphins()
    assert mo.foo.bar('spam')['eggs']
    assert mo.was_called()  # wrong method that passes
    assert mo.caled         # typo that passes!
    



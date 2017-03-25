import cng
from include.utilities.util import init_viewport, \
    init_window, \
    Point

if __name__ == '__main__':
    print 'test...'
    W_WIDTH = 800
    W_HEIGHT = 800

    # Window bottom left corner coordinates.
    W_MIN = Point(0, 0)
    # Window top right corner coordinates.
    W_MAX = Point(800, 800)

    # Create a window.
    init_window('TP1', W_MAX.x - W_MIN.x, W_MAX.y - W_MIN.y)

    # Viewport bottom left corner coordinates.
    V_MIN = Point(200, 200)
    # Viewport top right corner coordinates.
    V_MAX = Point(600, 600)
    init_viewport(V_MIN, V_MAX, 1)

    cng.main_loop()

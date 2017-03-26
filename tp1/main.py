#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

import cng
from include.utilities.util import init_viewport, \
    init_window, \
    Point, \
    window_viewport_mapping, \
    draw_mapping_list_point, \
    draw_point, \
    polynome

if __name__ == '__main__':
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

    p = (700, 20)
    draw_point(p)
    new_p = window_viewport_mapping(p, W_MIN, W_MAX, V_MIN, V_MAX)
    draw_point(new_p)

    draw_mapping_list_point(polynome(10, 250, 5000, [3, 3, 20]), W_MIN, W_MAX, V_MIN, V_MAX)

    cng.main_loop()

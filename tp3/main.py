#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

import cng

from include.utilities.util import init_viewport, \
    init_window, \
    mapping_list_point, \
    Point
import include.bezier as bezier

if __name__ == '__main__':
    # Window bottom left corner coordinates.
    W_MIN = Point(0, 0)
    # Window top right corner coordinates.
    W_MAX = Point(800, 800)

    # Create a window.
    init_window('TP2', W_MAX.x - W_MIN.x, W_MAX.y - W_MIN.y)

    # Viewport bottom left corner coordinates.
    V_MIN = Point(200, 200)
    # Viewport top right corner coordinates.
    V_MAX = Point(600, 600)
    init_viewport(V_MIN, V_MAX, 1)

    # Control points
    controls = [(0, 0), (0, 800), (800, 800), (800, 0)]
    #bezier.execute_bernstein(controls,
    #                         W_MIN, W_MAX, V_MIN, V_MAX)
    bezier.execute_casteljau(controls,
                   W_MIN, W_MAX, V_MIN, V_MAX)

    cng.main_loop()

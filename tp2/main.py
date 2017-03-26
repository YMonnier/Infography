#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

import cng
import time
from random import randint
from include.utilities.util import init_viewport, \
    init_window, \
    draw_mapping_point, \
    draw_mapping_list_point, \
    Point
import include.bresenham as bresenham

'''
    Create a random segments with bresenham algorithm.

    wMin: window bottom left corner coordinates
    wMax: window top rigth corner coordinates
    vMin: viewport bottom left corner coordinates
    vMax: viewport top rigth corner coordinates
    size: number of segment
'''


def random_bresemham_segment(wMin, wMax, vMin, vMax, size):
    for _ in range(size):
        a = Point(randint(wMin.x, wMax.x), randint(wMin.y, wMax.y))
        b = Point(randint(wMin.x, wMax.x), randint(wMin.y, wMax.y))

        draw_mapping_list_point(bresenham.generic(a, b),
                                wMin, wMax, vMin, vMax)


'''
    Create a random segments with naive algorithm.

    wMin: window bottom left corner coordinates
    wMax: window top rigth corner coordinates
    vMin: viewport bottom left corner coordinates
    vMax: viewport top rigth corner coordinates
    size: number of segment
'''


def random_naive_segment(wMin, wMax, vMin, vMax, size):
    for i in range(size):
        v1, v2 = randint(vMin.x, vMax.x) + 2 + i, randint(vMin.x, vMax.x) + 2 + i
        if v1 > v2:
            a = Point(v2, v2)
            b = Point(v1, v1)
        else:
            a = Point(v1, v1)
            b = Point(v2, v2)

        draw_mapping_list_point(bresenham.naive(a, b),
                                wMin, wMax, vMin, vMax)


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

    #
    # Bresenham tests
    #


    # Default | from (0,0) to (50, 50)
    # draw_mapping_list_point(bresenham.default(Point(50, 50)),
    #                        W_MIN, W_MAX, V_MIN, V_MAX)

    # Advanced | from point A to point B, first octant
    # draw_mapping_list_point(bresenham.advanced(Point(100, 100), Point(500, 500)),
    #                        W_MIN, W_MAX, V_MIN, V_MAX)
    # Advanced | from (0, 0) to point B, first and second octant.
    # draw_mapping_list_point(bresenham.two_octant(Point(10, 500)),
    #                        W_MIN, W_MAX, V_MIN, V_MAX)

    # Generic | from any point to any point

    '''
    draw_mapping_list_point(bresenham.generic(Point(400, 400), Point(500, 700)),
                            W_MIN, W_MAX, V_MIN, V_MAX)

    draw_mapping_list_point(bresenham.generic(Point(400, 400), Point(700, 500)),
                            W_MIN, W_MAX, V_MIN, V_MAX)

    draw_mapping_list_point(bresenham.generic(Point(400, 400), Point(700, 300)),
                            W_MIN, W_MAX, V_MIN, V_MAX)

    draw_mapping_list_point(bresenham.generic(Point(400, 400), Point(500, 100)),
                            W_MIN, W_MAX, V_MIN, V_MAX)

    draw_mapping_list_point(bresenham.generic(Point(400, 400), Point(300, 100)),
                            W_MIN, W_MAX, V_MIN, V_MAX)

    draw_mapping_list_point(bresenham.generic(Point(400, 400), Point(100, 300)),
                            W_MIN, W_MAX, V_MIN, V_MAX)

    draw_mapping_list_point(bresenham.generic(Point(400, 400), Point(100, 500)),
                            W_MIN, W_MAX, V_MIN, V_MAX)

    draw_mapping_list_point(bresenham.generic(Point(400, 400), Point(300, 700)),
                            W_MIN, W_MAX, V_MIN, V_MAX)
    '''


    # Start timer
    start_time = time.time()
    nbSegment = 1000
    print '**** Random %d segments with naive algo ****' % (nbSegment)
    random_naive_segment(W_MIN, W_MAX, V_MIN, V_MAX, nbSegment)
    print '	==> Execution time: %s seconds' % (time.time() - start_time)

    start_time = time.time()
    print '**** Random %d segments with bresenham algo ****' % (nbSegment)
    random_bresemham_segment(W_MIN, W_MAX, V_MIN, V_MAX, nbSegment)
    print '	==> Execution time: %s seconds' % (time.time() - start_time)

    cng.main_loop()

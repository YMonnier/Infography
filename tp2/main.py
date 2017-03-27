#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

import cng
import time
from random import randint
from include.utilities.util import init_viewport, \
    init_window, \
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
        a = (randint(wMin.x, wMax.x), randint(wMin.y, wMax.y))
        b = (randint(wMin.x, wMax.x), randint(wMin.y, wMax.y))

        bresenham.generic(a, b,
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
            a = (v2, v2)
            b = (v1, v1)
        else:
            a = (v1, v1)
            b = (v2, v2)

        bresenham.naive(a, b,
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
    # bresenham.default((50, 50),
    #                    W_MIN, W_MAX, V_MIN, V_MAX)

    # Advanced | from point A to point B, first octant
    # bresenham.advanced((100, 100), (500, 500),
    #                        W_MIN, W_MAX, V_MIN, V_MAX)
    # Advanced | from (0, 0) to point B, first and second octant.
    # bresenham.two_octant((10, 500),
    #                     W_MIN, W_MAX, V_MIN, V_MAX)

    # Generic | from any point to any point

    '''
    bresenham.generic((400, 400), (500, 700),
                      W_MIN, W_MAX, V_MIN, V_MAX)

    bresenham.generic((400, 400), (700, 500),
                      W_MIN, W_MAX, V_MIN, V_MAX)

    bresenham.generic((400, 400), (700, 300),
                      W_MIN, W_MAX, V_MIN, V_MAX)

    bresenham.generic((400, 400), (500, 100),
                      W_MIN, W_MAX, V_MIN, V_MAX)

    bresenham.generic((400, 400), (300, 100),
                      W_MIN, W_MAX, V_MIN, V_MAX)

    bresenham.generic((400, 400), (100, 300),
                      W_MIN, W_MAX, V_MIN, V_MAX)

    bresenham.generic((400, 400), (100, 500),
                      W_MIN, W_MAX, V_MIN, V_MAX)

    bresenham.generic((400, 400), (300, 700),
                      W_MIN, W_MAX, V_MIN, V_MAX)
    '''

    # Start timer
    start_time = time.time()
    nbSegment = 1000
    # print '**** Random %d segments with naive algo ****' % (nbSegment)
    # random_naive_segment(W_MIN, W_MAX, V_MIN, V_MAX, nbSegment)
    # print '	==> Execution time: %s seconds' % (time.time() - start_time)

    start_time = time.time()
    print '**** Random %d segments with bresenham algo ****' % (nbSegment)
    random_bresemham_segment(W_MIN, W_MAX, V_MIN, V_MAX, nbSegment)
    print '	==> Execution time: %s seconds' % (time.time() - start_time)

    cng.main_loop()

#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

import cng
from utilities.point import Point
from utilities.util import draw_point

'''
Default bresenham implementation.
Can draw a segment only into the first octant
from the ordinate (0, 0) to a specific point.
    point: target point
'''


def default(point):
    res = []
    dec = point.x - 2 * point.y
    x, y = 0, 0
    while x <= point.x:
        yield Point(x, y)
        #res.append(Point(x, y))
        if dec < 0:
            dec += 2 * point.x
            y += 1
        dec -= 2 * point.y
        x += 1


'''
Advanced bresenham implementation.
Can draw a segment only into the first octant
but with a specific ordinate.
    pointA: ordinate point.
    pointB: target point.
'''


def advanced(pointA, pointB):
    dx = pointB.x - pointA.x
    dy = pointB.y - pointA.y
    dec = dx - 2 * dy
    x, y = pointA.x, pointA.y
    while x <= dx:
        yield Point(x, y)
        if dec < 0:
            dec += 2 * dx
            y += 1
        dec -= 2 * dy
        x += 1


'''
Advanced bresenham implementation.
Can draw a segment only into the first octant
but with a specific ordinate.
    (dx, dy): target point.
'''


def two_octant(point):
    x, y = 0, 0
    if point.y > point.x:  # octant 2
        dec = point.y - 2 * point.x
        while y <= point.y:
            yield Point(x, y)
            if dec < 0:
                dec += 2 * point.y
                x += 1
            dec -= 2 * point.x
            y += 1
    else:  # octant 1
        dec = point.x - 2 * point.y
        while x <= point.x:
            yield Point(x, y)
            if dec < 0:
                dec += 2 * point.x
                y += 1
            dec -= 2 * point.y
            x += 1

#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

import cng
from utilities.point import Point

'''
    Naive drawing segment implementation.

    pointA: ordinate point (couple of abscissa and ordinate(x, y)).
    pointB: target point (couple of abscissa and ordinate(x, y)).
'''


def naive(pointA, pointB):
    dx = pointB.x - pointA.x
    dy = pointB.y - pointA.y

    y = pointA.y
    # print 'PointA(%d, %d)' % (pointA.x, pointA.y)
    # print 'PointB(%d, %d)' % (pointB.x, pointB.y)
    if (dx > 0):
        slope = dy / float(dx)

        point = Point(0, 0)
        for x in range(pointA.x, dx):
            yield (x, y)
            y += slope


'''
    Default bresenham implementation.
    Can draw a segment only into the first octant
    from the ordinate (0, 0) to a specific point.
        point: target point (couple of abscissa and ordinate(x, y))
'''


def default(point):
    res = []
    dec = point.x - 2 * point.y
    x, y = 0, 0
    while x <= point.x:
        yield (x, y)
        if dec < 0:
            dec += 2 * point.x
            y += 1
        dec -= 2 * point.y
        x += 1


'''
    Advanced bresenham implementation.
    Can draw a segment only into the first octant
    but with a specific ordinate.
        pointA: ordinate point (couple of abscissa and ordinate(x, y)).
        pointB: target point (couple of abscissa and ordinate(x, y)).
'''


def advanced(pointA, pointB):
    dx = pointB.x - pointA.x
    dy = pointB.y - pointA.y
    dec = dx - 2 * dy
    x, y = pointA.x, pointA.y
    while x <= dx:
        yield (x, y)
        if dec < 0:
            dec += 2 * dx
            y += 1
        dec -= 2 * dy
        x += 1


'''
    Advanced bresenham implementation.
    Can draw a segment only into the first octant
    but with a specific ordinate.
        (dx, dy): target point. couple of abscissa and ordinate(x, y)
'''


def two_octant(point):
    x, y = 0, 0
    if point.y > point.x:  # octant 2
        dec = point.y - 2 * point.x
        while y <= point.y:
            yield (x, y)
            if dec < 0:
                dec += 2 * point.y
                x += 1
            dec -= 2 * point.x
            y += 1
    else:  # octant 1
        dec = point.x - 2 * point.y
        while x <= point.x:
            yield (x, y)
            if dec < 0:
                dec += 2 * point.x
                y += 1
            dec -= 2 * point.y
            x += 1


'''
    Generic bresenham implementation.
    Can draw segment with any coordinates.
        (xa, ya): ordinate point (couple of abscissa and ordinate(x, y)).
        (xb, yb): target point (couple of abscissa and ordinate(x, y)).
'''


def generic(pointA, pointB):
    dx = pointB.x - pointA.x
    dy = pointB.y - pointA.y
    x, y = pointA.x, pointA.y

    x_direc = 1 if dx > 0 else -1  # move up or move down
    y_direc = 1 if dy > 0 else -1  # move up or move down

    dx = abs(pointB.x - pointA.x)
    dy = abs(pointB.y - pointA.y)

    if dy > dx:
        diff = dy
        dec = dy - 2 * dx
        dy = y + dy
        for i in range(diff):
            yield (x, y)
            if dec < 0:
                dec += 2 * dy
                x += x_direc
            dec -= 2 * dx
            y += y_direc
    else:
        diff = dx
        dec = dx - 2 * dy
        dx = x + dx
        for i in range(diff):
            yield (x, y)
            if dec < 0:
                dec += 2 * dx
                y += y_direc
            dec -= 2 * dy
            x += x_direc

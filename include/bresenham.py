#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

import cng
from utilities.point import Point
from utilities.util import window_viewport_mapping

'''
    Naive drawing segment implementation.

    pointA: ordinate point (couple of abscissa and ordinate(x, y)).
    pointB: target point (couple of abscissa and ordinate(x, y)).
    wMin: window bottom left corner coordinates
    wMax: window top rigth corner coordinates
    vMin: viewport bottom left corner coordinates
    vMax: viewport top rigth corner coordinates
'''


def naive(pointA, pointB,
          wMin, wMax, vMin, vMax):
    pointA = window_viewport_mapping(pointA, wMin, wMax, vMin, vMax)
    pointB = window_viewport_mapping(pointB, wMin, wMax, vMin, vMax)
    dx = pointB[0] - pointA[0]
    dy = pointB[1] - pointA[1]

    y = pointA[1]
    if dx > 0:
        slope = dy / float(dx)

        for x in range(pointA[0], dx):
            cng.point(x, y)
            y += slope


'''
    Default bresenham implementation.
    Can draw a segment only into the first octant
    from the ordinate (0, 0) to a specific point.

        point: target point (couple of abscissa and ordinate(x, y))
        wMin: window bottom left corner coordinates
        wMax: window top rigth corner coordinates
        vMin: viewport bottom left corner coordinates
        vMax: viewport top rigth corner coordinates
'''


def default(point,
            wMin, wMax, vMin, vMax):
    point = window_viewport_mapping(point, wMin, wMax, vMin, vMax)
    origin = window_viewport_mapping((0, 0), wMin, wMax, vMin, vMax)
    x, y = origin[0], origin[1]
    dec = point[0] - 2 * point[1]
    while x <= point[0]:
        cng.point(x, y)
        if dec < 0:
            dec += 2 * point[0]
            y += 1
        dec -= 2 * point[1]
        x += 1


'''
    Advanced bresenham implementation.
    Can draw a segment only into the first octant
    but with a specific ordinate.

        pointA: ordinate point (couple of abscissa and ordinate(x, y)).
        pointB: target point (couple of abscissa and ordinate(x, y)).
        wMin: window bottom left corner coordinates
        wMax: window top rigth corner coordinates
        vMin: viewport bottom left corner coordinates
        vMax: viewport top rigth corner coordinates
'''


def advanced(pointA, pointB,
             wMin, wMax, vMin, vMax):
    pointA = window_viewport_mapping(pointA, wMin, wMax, vMin, vMax)
    pointB = window_viewport_mapping(pointB, wMin, wMax, vMin, vMax)
    dx = pointB[0] - pointA[0]
    dy = pointB[1] - pointA[1]
    dec = dx - 2 * dy
    x, y = pointA[0], pointA[1]
    while x <= dx:
        cng.point(x, y)
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
        wMin: window bottom left corner coordinates
        wMax: window top rigth corner coordinates
        vMin: viewport bottom left corner coordinates
        vMax: viewport top rigth corner coordinates
'''


def two_octant(point,
               wMin, wMax, vMin, vMax):
    point = window_viewport_mapping(point, wMin, wMax, vMin, vMax)
    origin = window_viewport_mapping((0, 0), wMin, wMax, vMin, vMax)
    x, y = origin[0], origin[1]
    if point[1] > point[0]:  # octant 2
        dec = point[1] - 2 * point[0]
        while y <= point[1]:
            cng.point(x, y)
            if dec < 0:
                dec += 2 * point[1]
                x += 1
            dec -= 2 * point[0]
            y += 1
    else:  # octant 1
        dec = point[0] - 2 * point[1]
        while x <= point[0]:
            cng.point(x, y)
            if dec < 0:
                dec += 2 * point[0]
                y += 1
            dec -= 2 * point[1]
            x += 1


'''
    Generic bresenham implementation.
    Can draw segment with any coordinates.
        (xa, ya): ordinate point (couple of abscissa and ordinate(x, y)).
        (xb, yb): target point (couple of abscissa and ordinate(x, y)).
        wMin: window bottom left corner coordinates
        wMax: window top rigth corner coordinates
        vMin: viewport bottom left corner coordinates
        vMax: viewport top rigth corner coordinates
'''


def generic(pointA, pointB,
            wMin, wMax, vMin, vMax):
    pointA = window_viewport_mapping(pointA, wMin, wMax, vMin, vMax)
    pointB = window_viewport_mapping(pointB, wMin, wMax, vMin, vMax)
    dx = pointB[0] - pointA[0]
    dy = pointB[1] - pointA[1]
    x, y = pointA[0], pointA[1]

    x_direc = 1 if dx > 0 else -1  # move right or move left
    y_direc = 1 if dy > 0 else -1  # move up or move down

    dx = abs(pointB[0] - pointA[0])
    dy = abs(pointB[1] - pointA[1])

    if dy > dx:
        diff = dy
        dec = dy - 2 * dx
        dy = y + dy
        for i in range(diff):
            cng.point(x, y)
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
            cng.point(x, y)
            if dec < 0:
                dec += 2 * dx
                y += y_direc
            dec -= 2 * dy
            x += x_direc

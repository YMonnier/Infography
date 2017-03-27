#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

import cng
from point import Point

'''
    Initialize the window.

    name: Name window.
    width: Width window.
    height: Height window.
'''


def init_window(name, width, height):
    cng.init_window(name,
                    width,
                    height)


'''
    Initialize the viewport.

    pMin: Bottom left corner coordinates.
    pMax: Top rigth corner coordinates.
'''


def init_viewport(pMin, pMax, size):
    cng.rectangle(pMin.x, pMin.y, pMax.x, pMax.y, size)


'''
    Draw a polynomial curve.

    xmin: x min abscissa.
    xmax: x max abscissa.
    size: Number of point.
    coeffs: Polynomial coefficients.
'''


def polynome(xmin, xmax, size, coeffs):
    step = (xmax - xmin) / float(size)
    x_i = xmin
    while x_i < xmax:
        y = __horner(x_i, coeffs)
        yield (x_i, y)
        x_i += step


'''
    Horner function.

    factor: Factor.
    coeffs: List of coefficient.
'''


def __horner(factor, coeffs):
    res = coeffs[0]
    for a in range(1, len(coeffs) - 1):
        res = res * factor + coeffs[a]
    return res


'''
    window_viewport_mapping function.

    Convert a point from continuous state space to discrete.

    point: Point to map. (couple of abscissa and ordinate(x, y))
    wMin: window bottom left corner coordinates
    wMax: window top rigth corner coordinates
    vMin: viewport bottom left corner coordinates
    vMax: viewport top rigth corner coordinates
'''


def window_viewport_mapping(point, wMin, wMax, vMin, vMax):
    xv = vMax.x - vMin.x
    xw = wMax.x - wMin.x
    yv = vMax.y - vMin.y
    yw = wMax.y - wMin.y

    x = int(point[0] * (xv / float(xw)) + (xv * (-wMin.x)) + vMin.x)
    y = int(point[1] * (yv / float(yw)) + (yv * (-wMin.y)) + vMin.y)

    return (x, y)


def mapping_list_point(list, wMin, wMax, vMin, vMax):
    return map(lambda p: window_viewport_mapping(p, wMin, wMax, vMin, vMax),
        list)


'''
    Apply window viewport mapping from a list of point.

    list: List of couple of abscissa and ordinate(x, y)
    wMin: window bottom left corner coordinates
    wMax: window top rigth corner coordinates
    vMin: viewport bottom left corner coordinates
    vMax: viewport top rigth corner coordinates
'''


def draw_mapping_list_point(list, wMin, wMax, vMin, vMax):
    for p in list:
        draw_mapping_point(p, wMin, wMax, vMin, vMax)
        # map(lambda p: draw_mapping_point(p, wMin, wMax, vMin, vMax),
        #    list)


'''
    Draw a point with the window viewport mapping.

    point: Point to display, couple of abscissa and ordinate(x, y).
    wMin: window bottom left corner coordinates
    wMax: window top rigth corner coordinates
    vMin: viewport bottom left corner coordinates
    vMax: viewport top rigth corner coordinates
'''


def draw_mapping_point(point, wMin, wMax, vMin, vMax):
    (x, y) = window_viewport_mapping(point, wMin, wMax, vMin, vMax)
    cng.point(x, y)


def draw_point(point):
    cng.point(point[0], point[1])

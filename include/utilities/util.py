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
    windowToViewportMapping function.

    point: Point to map.
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

    x = int(point.x * ((xv) / float(xw)) + ((xv) * (-wMin.x)) + vMin.x)
    y = int(point.y * ((yv) / float(yw)) + ((yv) * (-wMin.y)) + vMin.y)

    return Point(x, y)

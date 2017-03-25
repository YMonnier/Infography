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
    window_viewport_mapping function.

    Convert a point from continuous state space to discrete.

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

    x = int(point.x * (xv / float(xw)) + (xv * (-wMin.x)) + vMin.x)
    y = int(point.y * (yv / float(yw)) + (yv * (-wMin.y)) + vMin.y)

    return Point(x, y)


'''
    Apply window viewport mapping from a list of point.

    list: List of Point
    wMin: window bottom left corner coordinates
    wMax: window top rigth corner coordinates
    vMin: viewport bottom left corner coordinates
    vMax: viewport top rigth corner coordinates
'''


def draw_mapping_list_point(list, wMin, wMax, vMin, vMax):
    map(lambda p: draw_mapping_point(p, wMin, wMax, vMin, vMax),
        list)


'''
    Draw a point with the window viewport mapping.

    point: Point to display.
    wMin: window bottom left corner coordinates
    wMax: window top rigth corner coordinates
    vMin: viewport bottom left corner coordinates
    vMax: viewport top rigth corner coordinates
'''


def draw_mapping_point(point, wMin, wMax, vMin, vMax):
    point = window_viewport_mapping(point, wMin, wMax, vMin, vMax)
    cng.point(point.x, point.y)


def draw_point(point):
    cng.point(point.x, point.y)

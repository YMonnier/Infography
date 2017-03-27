#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
import cng
from utilities.util import mapping_list_point


def __factorial(n):
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res


'''
    Bernstein function
    Calculate the berstein p-eme polynom
    with the order n in t.

    p: polynome number
    n: order
    t

'''


def __bernstein(n, p, t):
    result = __factorial(n) / (__factorial(p) * __factorial(n - p)) * t ** p * (1 - t) ** (n - p)
    return result


'''
    Calculate the points on curve bezier.
'''


def __compute_point(position, points):
    x, y = 0, 0
    size = len(points)
    for i in range(size):
        x += (__bernstein(size - 1, i, position) * points[i][0])
        y += (__bernstein(size - 1, i, position) * points[i][1])
    return x, y


'''
    Execute the Bezier algorithm

    points: Control points.
    wMin: window bottom left corner coordinates
    wMax: window top rigth corner coordinates
    vMin: viewport bottom left corner coordinates
    vMax: viewport top rigth corner coordinates
'''


def execute(points,
            wMin, wMax, vMin, vMax):
    points = mapping_list_point(points,
                                wMin, wMax, vMin, vMax)
    step = 0.01
    k = 0
    res = []
    while k < 1:
        res.append(__compute_point(k, points))
        k += step
    for i in range(len(res) - 1):
        cng.line(res[i][0], res[i][1],
                 res[i + 1][0], res[i + 1][1])

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
    Using bernstein method.
'''


def __compute_point_bernstein(position, points):
    if len(points) != 4:
        raise SystemExit("Should have 4 control points")
    x, y = 0, 0
    size = len(points)
    for i in range(size):
        x += (__bernstein(size - 1, i, position) * points[i][0])
        y += (__bernstein(size - 1, i, position) * points[i][1])
    return x, y


'''
    Calculate the points on curve bezier.
    Using Casteljau method(barycenter).
'''


def __compute_point_casteljau(position, points):
    if len(points) != 4:
        raise SystemExit("Should have 4 control points")
    delta = (1 - position)
    p1 = delta * points[0][0] + position * points[1][0], \
         delta * points[0][1] + position * points[1][1]
    p2 = delta * points[1][0] + position * points[2][0], \
         delta * points[1][1] + position * points[2][1]
    p3 = delta * points[2][0] + position * points[3][0], \
         delta * points[2][1] + position * points[3][1]
    p4 = delta * p1[0] + position * p2[0], \
         delta * p1[1] + position * p2[1]
    p5 = delta * p2[0] + position * p3[0], \
         delta * p2[1] + position * p3[1]
    return delta * p4[0] + position * p5[0], \
           delta * p4[1] + position * p5[1]


'''
    Execute the Bezier algorithm using casteljau.

    points: Control points.
    wMin: window bottom left corner coordinates
    wMax: window top rigth corner coordinates
    vMin: viewport bottom left corner coordinates
    vMax: viewport top rigth corner coordinates
'''


def execute_casteljau(points,
                                wMin, wMax, vMin, vMax):
    points = mapping_list_point(points,
                                wMin, wMax, vMin, vMax)
    print(points)
    step = 0.01
    k = 0
    res = []
    while k < 1.0:
        res.append(__compute_point_casteljau(k, points))
        k += step
    for i in range(len(res) - 1):
        cng.line(res[i][0], res[i][1],
                 res[i + 1][0], res[i + 1][1])


'''
    Execute the Bezier algorithm using bernstein.

    points: Control points.
    wMin: window bottom left corner coordinates
    wMax: window top rigth corner coordinates
    vMin: viewport bottom left corner coordinates
    vMax: viewport top rigth corner coordinates
'''


def execute_bernstein(points,
                      wMin, wMax, vMin, vMax):
    points = mapping_list_point(points,
                                wMin, wMax, vMin, vMax)
    step = 0.01
    k = 0
    res = []
    while k < 1:
        res.append(__compute_point_bernstein(k, points))
        k += step
    for i in range(len(res) - 1):
        cng.line(res[i][0], res[i][1],
                 res[i + 1][0], res[i + 1][1])

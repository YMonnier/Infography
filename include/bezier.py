#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
import cng


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
'''


def execute(points):
    step = 0.01
    k = 0
    while k < 1:
        yield __compute_point(k, points)
        k += step


'''
    Draw the curve Bezier

    points: Bezier points.
'''


def display(points):
    for i in range(len(points) - 1):
        cng.line(points[i][0], points[i][1],
                 points[i + 1][0], points[i + 1][1])

#!/usr/bin/python2.7
# -*- coding: utf-8 -*-


def factorial(n):
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res


# Calcul de B_(n,p) (t) le p-eme polynome de Bernstein d'ordre n, en t
def bernstein(n, p, t):
    result = factorial(n) / (factorial(p) * factorial(n - p)) * t ** p * (1 - t) ** (n - p)
    return result


# Calcul du point sur la courbe de Bezier s'appuyant sur les points du tableau points en u
def calcPoint(u, points):
    res = 0
    for i in range(len(points)):
        res += (bernstein(len(points), i, u) * points[i])
    return res


def execute(myXs, myYs):
    xCurb = []
    yCurb = []

    # pas du trace entre 0 et 1
    pas = 0.01

    k = 0

    # On fait varier le param de trace entre 0 et 1
    while (k < 1):
        # Calcul du point de la courbe en k
        x = calcPoint(k, myXs)
        y = calcPoint(k, myYs)

        # On ajoute les points calcules dans la liste des points de la courbe
        #xCurb.append(x)
        #yCurb.append(y)
        yield (x, y)
        k += pas
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
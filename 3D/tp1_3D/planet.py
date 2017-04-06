#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

###############################################################
# portage de planet.c

from OpenGL.GL import *  # exception car prefixe systematique
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys

###############################################################
# variables globales
year, day = 0, 0
quadric = None

###############################################################
#

'''
    Initialisation de la scène.
'''


def init():
    global quadric
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glShadeModel(GL_SMOOTH)
    quadric = gluNewQuadric()
    gluQuadricDrawStyle(quadric, GLU_FILL)
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_COLOR_MATERIAL)
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    # Directional light
    glLightfv(GL_LIGHT0, GL_POSITION, [200, 200, 0, 1])


'''
    Construction des deux sphères.
'''


def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glPushMatrix()

    # Sun section
    glColor4f(1.000, 1.000, 0.000, 1.0)
    gluSphere(quadric, 0.5, 100, 100)

    glPushMatrix()
    # Earth section
    glRotatef(year, 0.0, 2.0, 0.0)
    glTranslatef(1.75, 0.0, 0.0)
    glRotatef(day, 0.0, 1.0, 0.0)

    glColor4f(0.118, 0.565, 1.000, 1.0)
    gluSphere(quadric, 0.225, 10, 16)

    # Moon section
    glTranslatef(0.5, 0.0, 0.0)
    glColor4f(0.663, 0.663, 0.663, 1.0)
    gluSphere(quadric, 0.09, 10, 16)

    glPopMatrix()

    glPopMatrix()

    glutSwapBuffers()

    '''
    glPushMatrix()

    # Transfert du repère de travail vers celui centré sur la planète
    glRotatef(year, 0.0, 1.0, 0.0)
    glTranslatef(3.0, 0.0, 0.0)
    glRotatef(day, 0.0, 1.0, 0.0)

    # Planète 1 (violet)
    glColor4f(1.0, 0, 1.0, 1.0)
    gluSphere(quadric, 0.3, 10, 16)

    glColor4f(0, 1.0, 0, 1.0)
    gluSphere(quadric, 0.2, 10, 16)

    glPopMatrix()
    '''


'''
    Updating the window dimensions
'''


def reshape(width, height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    if width <= height:
        glOrtho(-2.5, 2.5, -2.5 * height / width, 2.5 * height / width, -10.0, 10.0)
    else:
        glOrtho(-2.5 * width / height, 2.5 * width / height, -2.5, 2.5, -10.0, 10.0)
    glMatrixMode(GL_MODELVIEW)


'''
    Keyboard event.
'''


def keyboard(key, x, y):
    global day, year
    if key == 'j':
        day = (day + 10) % 360
    elif key == 'J':
        day = (day + 10) % 360
    elif key == 'a':
        year = (year + 5) % 360
    elif key == 'A':
        year = (year + 5) % 360
    elif key == '\033':
        sys.exit()
    glutPostRedisplay()  # indispensable en Python


###############################################################
# MAIN

glutInit()
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH)

glutCreateWindow('planet')
glutReshapeWindow(1024, 800)

glutReshapeFunc(reshape)
glutDisplayFunc(display)
glutKeyboardFunc(keyboard)

init()

glutMainLoop()

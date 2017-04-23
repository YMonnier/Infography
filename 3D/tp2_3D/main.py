#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

#
# ############################
# ############################
#
# Author @YMonnier
# https://github.com/YMonnier/Infography
# Project 3D/TP2
#
# Program allowing to manipulate
# a cannon and fire a cannonball. :-)
#
# How to use it?
#
# --> Keys on your keyboard :O ...
#
# Cannon movement:
#   - up arrow: cannon goes straight
#   - down arrow: cannon goes back
#   - right arrow: right cannon rotation.
#   - left arrow: left cannon rotation.
#   - f: cannon up (inclination)
#   - g: cannon down (inclination)
#
# Camera movement:
#   - s: up camera.
#   - x: down camera.
#   - c: right camera.
#   - w: left camera.
#
# Actions:
#   - space key: fire action!
#   - r key: reset the cannonball.
#
# If you want to change the keyboard
# settings go to the `keyboard` function and change the keys code.
#
# Program using OpenGL library.
#
# ############################
# ############################
#

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math

quadric = None

# gluLookAt center position.
centerX, centerY, centerZ = -1.0, 0.0, 0.0

# constants.
upX, upY, upZ = 0.0, 1.0, 0.0
eyeX, eyeY, eyeZ = -2.0, 1.5, 1

# Cannon movements.
cannon_left_right, cannon_up_down = 0, 0

# Cannon inclination.
cannon_inclination = 0

# Cannon rotation. (left, right, back, straight)
cannon_rotation = 0

t = 0

'''
    Scene initialization.
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


'''
    Window dimension updating.
'''


def reshape(width, height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    if width <= height:
        glOrtho(-2.5, 2.5, -2.5 * height / width, 2.5 * height / width, -10.0, 100.0)
    else:
        glOrtho(-2.5 * width / height, 2.5 * width / height, -2.5, 2.5, -10.0, 100.0)
    glMatrixMode(GL_MODELVIEW)


'''
    Keyboard event to
    manipulate camera and cannon.

    * Camera
        * s: up camera.
        * x: down camera.
        * c: right camera.
        * w: left camera.

    * Cannon
        * up arrow: cannon goes straight
        * down arrow: cannon goes back
        * right arrow: right cannon rotation.
        * left arrow: left cannon rotation.
        * f: cannon up (inclination)
        * g: cannon down (inclination)

    *Actions:
        * space key: fire action!
        * r: reset the cannonball.
'''


def keyboard(key, x, y):
    global centerX, centerY, centerZ
    global cannon_up_down, cannon_left_right, cannon_rotation, cannon_inclination, t
    step = 0.35
    cannon_step = 0.02
    print key
    if key == '\033':
        sys.exit()
    elif key == 115:  # s: up camera
        centerY += step
    elif key == 120:  # x: down camera
        centerY -= step
    elif key == 99:  # c: right camera
        centerX += step
    elif key == 119:  # w: left camera
        centerX -= step
    elif key == 101:  # up arrow: cannon goes straight
        cannon_left_right += cannon_step
        cannon_rotation = 0
    elif key == 103:  # down arrow: cannon goes back
        cannon_left_right -= cannon_step
        cannon_rotation = 180
    elif key == 100:  # left arrow: cannon left
        cannon_up_down -= cannon_step
        cannon_rotation = 90
    elif key == 102:  # right arrow: cannon right
        cannon_up_down += cannon_step
        cannon_rotation = -90
    elif key == 108:  # f: cannon up
        cannon_inclination += 1
    elif key == 109:  # g: cannon down
        cannon_inclination += 1
    elif key == 32:
        t += 0.05
    elif key == 114:
        t = 0
    glutPostRedisplay()


def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glColor4f(1.0, 1.0, 1.0, 1.0)

    glPushMatrix()

    # Camera
    gluLookAt(eyeX, eyeY, eyeZ, centerX, centerY, centerZ, 0.0, 1.0, 0.0)

    height_ground = 0.3
    __setup_ground(height_ground)
    __setup_cannon(height_ground)

    glPopMatrix()

    glutSwapBuffers()


'''
    Define the scene ground.

    height_ground: Height ground.
'''


def __setup_ground(height_ground):
    sand_area_1_width = 1
    sand_area_2_width = 1
    water_area_width = 1

    # First block
    glPushMatrix()
    glColor4f(0.855, 0.647, 0.125, 1.0)  # Sand color
    glScalef(1, height_ground, 2)
    glutSolidCube(sand_area_1_width)
    glPopMatrix()

    # Middle block
    glPushMatrix()
    glTranslatef(sand_area_1_width, 0.0, 0.0)
    glScalef(1, height_ground - (height_ground * 0.35), 2)
    glColor4f(0.098, 0.098, 0.439, 1.0)  # Water color
    glutSolidCube(water_area_width)
    glPopMatrix()

    # Last block
    glPushMatrix()
    glTranslatef(water_area_width * 2, 0.0, 0.0)
    glScalef(1, height_ground, 2)
    glColor4f(0.855, 0.647, 0.125, 1.0)  # Sand color
    glutSolidCube(sand_area_2_width)
    glPopMatrix()


'''
    Define the cannon.
    Define orientation cannon.

    The cannon is created with two
    wheels and a cylinder.
    Moreover, defining the fire action (see `fire`function).

    height_ground: Height ground.
'''


def __setup_cannon(height_ground):
    glPushMatrix()

    # Translate on the top of the ground and defining the cannon movements.
    # see 'cannon_left_right' and 'cannon_up_down' actions from keyboard functions.
    glTranslatef(cannon_left_right, height_ground - (height_ground * 0.175), cannon_up_down)

    glTranslate(0, -0.5, 0)  # default position
    glRotate(cannon_rotation, 0, 1, 0)  # Cannon rotation.
    glTranslate(0, 0.5, 0)

    # Cannon properties
    glScalef(0.02, 0.02, 0.02)
    glColor4f(0.698, 0.133, 0.133, 1)

    # Create the first wheel.
    glPushMatrix()
    glTranslatef(0, 0, 3.5)
    glutSolidTorus(1.0, 3.0, 100, 100)
    glPopMatrix()

    # Create the second wheel.
    glPushMatrix()
    glTranslatef(0, 0, -3.5)
    glutSolidTorus(1.0, 3.0, 100, 100)
    glPopMatrix()

    # Main structure.

    glPushMatrix()
    glRotate(90, 0, 1, 0)
    glRotate(cannon_inclination, 1, 0, 0)  # Cannon inclination (Up - Down)
    # gluCylinder(gluNewQuadric(), 2.6, 1.5, 13, 100, 100)
    gluCylinder(gluNewQuadric(), 3, 3.5, 13, 100, 100)
    glPopMatrix()

    glPushMatrix()
    gluSphere(gluNewQuadric(), 3.0, 50, 16)
    glPopMatrix()

    __fire()

    glPopMatrix()


def __fire():
    global t
    alpha = -cannon_inclination * 2 * math.pi / 360
    v0 = 55
    m = 1
    g = 9.81
    k = 0.000018 * 6 * math.pi * 2.8 / 2
    my_const = v0 * math.sin(alpha) + (g * m) / k
    my_z = (m / k) * (my_const * (1 - math.exp(-k * t / m)) - g * t)

    glPushMatrix()
    glColor4f(0, 0, 0, 1)
    glTranslate((math.cos(alpha) * v0 * t - (m / k) * (math.exp(-k * t / m) - 1)), max(my_z, 0), 0)
    gluSphere(gluNewQuadric(), 2.8, 50, 16)
    glPopMatrix()


#
# Basic settings.
# Main.
#
glutInit()
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH)

glutCreateWindow('Cannon - TP2 - 3D - YMonnier')
glutReshapeWindow(1200, 800)

glutReshapeFunc(reshape)
glutDisplayFunc(display)
glutSpecialFunc(keyboard)

init()

glutMainLoop()

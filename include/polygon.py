import cng
from utilities.util import mapping_list_point

'''
    Draw a polygon depending on vertices passed in parameter.

    vertices: list of vertex.
    wMin: window bottom left corner coordinates
    wMax: window top rigth corner coordinates
    vMin: viewport bottom left corner coordinates
    vMax: viewport top rigth corner coordinates
'''


def create(vertices,
           wMin, wMax, vMin, vMax):
    vertices = mapping_list_point(vertices,
                                  wMin, wMax, vMin, vMax)
    for i in range(len(vertices)):
        cng.line(vertices[i][0], vertices[i][1],
                 vertices[i + 1][0], vertices[i + 1][1])

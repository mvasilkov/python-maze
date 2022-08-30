#!/usr/bin/env python
"""
Draw an image of the maze on the screen

MIT License

Copyright (c) 2017 Gaurav Mathur

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE.
"""

import pygame
import sys
from pygame.locals import *
from grid import Grid
from cell import Cell

COLOR_RAVEN = (102, 116, 128)
COLOR_SEPIA = (245, 223, 201)
COLOR_CORAL = (255, 127, 80)
COLOR_DARKSLATEGRAY = (47, 79, 79)
COLOR_DARKSLATEBLUE = (72, 61, 139)
COLOR_DARKORANGE = (255, 140, 0)
COLOR_LIGHTSEAGREEN = (32, 178, 170)

class MazeDraw:
    def __init__(self, grid, title):
        self.nRows, self.nColumns = grid.dimensions()
        self.CW = 12
        self.CH = 12
        self.XMARGIN = 20
        self.YMARGIN = 120
        self.WW = self.CW * self.nColumns + self.XMARGIN
        self.WH = self.CH * self.nRows + self.YMARGIN
        self.grid = grid
        self.title = title

    def draw(self):

        pygame.init()
        BIT_COLOR_32 = 32
        SURFACE = pygame.display.set_mode((self.WW, self.WH), pygame.RESIZABLE, BIT_COLOR_32)
        pygame.display.set_caption(self.title)

        SURFACE.fill(COLOR_SEPIA)

        save_img = pygame.image.load('images/save.png')
        save_img = pygame.transform.scale(save_img, (20, 20))

        SURFACE.blit(save_img, (8, 8))
        yoff = self.YMARGIN/2 # x offset
        for row in self.grid.each_row():
            xoff = self.XMARGIN/2 # y offset
            for cell in row:
                if cell is not None:
                    #if self.grid.crumbs[cell] is not None:
                    #    pygame.draw.circle(SURFACE, COLOR_CORAL, (xoff+self.CW/2, yoff+self.CH/2), 2, 0)
                    if not cell.isLinked(cell.cellNorth):
                        pygame.draw.line(SURFACE, COLOR_RAVEN, (xoff, yoff), (xoff+self.CW, yoff), 4)
                    if not cell.isLinked(cell.cellSouth):
                        pygame.draw.line(SURFACE, COLOR_RAVEN, (xoff, yoff+self.CH), (xoff+self.CW, yoff+self.CH), 4)
                    if not cell.isLinked(cell.cellWest):
                        pygame.draw.line(SURFACE, COLOR_RAVEN, (xoff, yoff), (xoff, yoff+self.CH), 4)
                    if not cell.isLinked(cell.cellEast):
                        pygame.draw.line(SURFACE, COLOR_RAVEN, (xoff+self.CW, yoff), (xoff+self.CW, yoff+self.CH), 4)
                xoff = xoff + self.CW
            yoff = yoff + self.CH


        while True:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    if save_img.get_rect().collidepoint(x, y):
                        pygame.image.save(SURFACE, 'maze.png')
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
            pygame.display.update()

if __name__ == "__main__":
        g = Grid(10, 10)
        MazeDraw(g).draw()

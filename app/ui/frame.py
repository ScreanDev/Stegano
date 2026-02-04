# coding: utf-8
 
from tkinter import *

class Frame:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
    

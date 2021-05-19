from tkinter import *
import threading

# Determines if a root element has bee created already
hasRoot = False


class Window:
    def __init__(self):
        global hasRoot
        if not hasRoot:
            hasRoot = True
            self.__internal = Tk()
        else:
            self.__internal = Tcl()

        self.__components = []

    def update(self):
        pass

    def get_internal(self):
        return self.__internal

    def get_components(self):
        return self.__components

    def add_component(self, component):
        self.__components.append(component)

    def pack_all(self):
        for component in self.__components:
            component.pack()

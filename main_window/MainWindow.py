from tkinter import Canvas
from common.util.Window import Window
from random import randint


class MainWindow(Window):
    def __init__(self):
        super().__init__()
        self.__panel = super().get_internal()
        self.__panel.title('Map Editor')
        self.__canvas = Canvas()
        self.__entities = []
        self.load_components()

    def load_components(self):
        self.__canvas = Canvas(self.__panel, height=750, width=750)
        self.add_component(self.__canvas)
        self.__entities.append(self.__canvas.create_oval(randint(0, 200), randint(0, 200), 0, 0, fill='#FF0000'))
        super().pack_all()

    def update(self):
        x1, y1, x2, y2 = self.__canvas.coords(self.__entities[0])
        x2, y2 = x1 + randint(0, 200), y1 + randint(0, 200)
        self.__canvas.coords(self.__entities[0], x1, y1, x2, y2)

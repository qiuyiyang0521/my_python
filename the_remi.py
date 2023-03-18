# -*- coding:utf-8 -*-
from turtle import width
from typing import Container
import remi

class MyApp(remi.App):
    def __init__(self, *args):
        super(MyApp, self).__init__(*args)
        self.bt = ""
        self.lbl = ""

    def main(self):
        container = remi.gui.VBox(width=300, height=300)
        self.lbl = remi.gui.Label("Hello world!")
        self.bt = remi.gui.Button("Press me!")

        # setting the listener for the onclick event of the button
        self.bt.onclick.do(self.on_button_pressed)

        container.append(self.lbl)
        container.append(self.bt)

        return container

    def on_button_pressed(self, widget):
        self.lbl.set_text('Button pressed!')
        self.bt.set_text('Hi!')


remi.start(MyApp)

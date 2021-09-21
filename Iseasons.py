#!/usr/bin/env python3.9
import PySimpleGUI as sg
import random


class Iseasons():

    def __init__(self, winname = 'Seasons') -> None:
        self.winname = winname
        self.arr = []
        self.btn = sg.Button('Roll', key='_GO_')
        self.lauer = [self.arr, [self.btn]]
        self.win = sg.Window(self.winname, self.lauer)

    def renderdice(self, num, puth):
        for i in range(num):
            self.arr.append(sg.Image(puth[i], key=f'{i}'))
    

    def renderdiceupdate(self, num, puth):
        for i in range(num):
            self.win[f'{i}'].update(filename=f'img/{a}.png')


win = Iseasons()
while True:
    event, values = win.win.read()
    if event in (None, 'Exit', 'Cancel'):
        break
    if event == '_GO_':
        for i in range(5):
            a = random.randint(1, 6)
            win[f'{i}'].update(filename=f'img/{a}.png')
win.close()

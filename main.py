# -*- coding: utf-8 -*-
from os import name
from tkinter import image_names
import PySimpleGUI as sg 
from Game import Game
#from Iseasons import Iseasons

def win1():
    lauer1 = [[sg.T('Сколько будет играть человек?'), sg.Combo(['2', '3', '4'], default_value='2', key='_PL_')], 
                [sg.Button('Старт', key='_START_')]
            ]
    w1 = sg.Window('Сезоны Начало', lauer1)
    while True:
        event, values = w1.read()
        if event in (None, 'Exit', 'Cancel'):
            break
        if event == '_START_':
            num_gamers = int(values['_PL_'])
            break
    w1.close()
    return num_gamers

def win2(num_gamers):
    arr = []
    names_gamers = []
    for i in range(num_gamers):
        arr.append([sg.T(f'Игрок №{i+1}'), sg.Input(key=f'{i}')])
    lauer2 = [arr, [sg.Button('Старт', key='_START_')]]
    w2 = sg.Window('Сезоны Знакомство', lauer2)
    while True:
        event, values = w2.read()
        if event in (None, 'Exit', 'Cancel'):
            break
        if event == '_START_':
            for j in range(num_gamers):
                names_gamers.append(values[f'{j}'])
            break
    w2.close()
    return names_gamers

def win3(names_gamers):
    s = ''
    for i in names_gamers:
        s += i.name + '\n'
    sg.popup(f'Сядьте в следующем порядке:\n{s}И начинайте спокойно играть.')

def winroll(g, arr, v, w1, name):
    g.roll_dices()
    for i in range(len(arr)):
        if v[f'{i}c'] == '':
            tt=g.dices[i][1]
            g.cal.time(tt)
        arr[i][1].Update(filename=g.dices[i][0])
        w1[f'{i}c'].update(values=name)
    w1['data'].update(f'{g.cal.get_year()} год {g.id_season_to_season()}')
    

def win4(g):
    """Косячный недоделанный метод"""
    text_data = f'{g.cal.get_year()} год {g.id_season_to_season()}'
    g.roll_dices()
    arr = []
    ev = []
    name = []
    for i in g.gamers:
        name.append([i.name])
    name.append('')
    for i in range(g.num_dice_in_season):
        arr.append([
                    sg.Combo(name, default_value='', key=f'{i}c'), 
                    sg.Image(g.dices[i][0], key=i), 
                    sg.Button('Перебросить', key=f'{i}b')
                    ])
        ev.append(f'{i}b')
    lauer1 = [[sg.Text(text_data, key='data')], [arr], [sg.Button('Бросок', key='_ROLL_')]]
    w1 = sg.Window('Сезоны', lauer1)
    while True:
        event, values = w1.read()
        if event in (None, 'Exit', 'Cancel'):
            break
        if event == '_ROLL_':
            winroll(g, arr, values, w1, name)
        if event in ev:
            g.roll_dices()
            j = int(event[:1])
            w1[j].update(filename=g.dices[j][0])
    w1.close()

num_gamers = win1()
g = Game(num_gamers)
g.create_players(win2(num_gamers))
win3(g.gamers)
win4(g)

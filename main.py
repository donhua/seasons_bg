# -*- coding: utf-8 -*-
from os import name
import PySimpleGUI as sg 
from Game import Game


def win1():
    """Создает окно, которое запрашивает количество игроков"""
    lauer1 = [
              [
                sg.T('Сколько будет играть человек?'), 
                sg.Combo(  
                         ['2', '3', '4'], 
                         default_value='2', 
                         key='_PL_'
                         )
              ], 
                [sg.Button('Старт',
                           key='_START_'
                           )
                 ]
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
    """Создает окно. Принимает количество игроков, возвращает список имен игроков"""
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
    """Создает окно. Предлагает рассадку игроков"""
    s = ''
    for i in names_gamers:
        s += i.name + '\n'
    sg.popup(f'Сядьте в следующем порядке:\n{s}И начинайте спокойно играть.')

def win4(g):
    """Окно с циклом игры"""
    g.roll_dices()
    arr = []
    ev = []
    name = []
    for i in g.gamers:
        name.append([i.name])
    name.append('')
    for i in range(g.num_gamers+1):
        arr.append([
                    sg.Combo(name, default_value='', key=f'{i}c'), 
                    sg.Image(g.dices[i][0], key=i), 
                    sg.Button('Перебросить', key=f'{i}b')
                    ])
        ev.append(f'{i}b')
    lauer1 = [[sg.Text(g.text_time(), key='data')], 
              [arr], 
              [sg.Button('Бросок', key='_ROLL_')]]
    w1 = sg.Window('Сезоны', lauer1)
    while True:
        event, values = w1.read()
        if event in (None, 'Exit', 'Cancel'):
            break
        if event == '_ROLL_':
            if g.time_end() == True:
                sg.popup('Закончился третий год. Конец игры.')
                break
            #winroll(g, arr, values, w1, name)
            for i in range(len(arr)):
                if values[f'{i}c'] == '':
                    g.time(g.dices[i][1])
            g.roll_dices()
            for i in range(len(arr)):
                arr[i][1].Update(filename=g.dices[i][0])
                w1[f'{i}c'].update(values=name)
            w1['data'].update(g.text_time())
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

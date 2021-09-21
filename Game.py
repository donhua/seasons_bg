import json
import random
from pathlib import Path
from S_Calendar import S_Calendar
from Player import Player


class Game:

    def __init__(self, num_gamers: int, path_setting: str = 'settings.json', path_image: str = 'img'):
        self.num_gamers = num_gamers
        self.num_dice_in_season = self.num_gamers + 1
        self.cal = S_Calendar()
        self.p_settings = path_setting
        self.p_img = path_image
        self.data = self.j()
        self.dices = []
        self.gamers = []

    def j(self):
        """Парсим настройки"""
        with open(self.p_settings, 'r', encoding='utf-8') as j:
            return json.load(j)

    def game_over(self):
        """Проверяет окончание третьего года игры"""
        if self.cal.get_year() == 4:
            return True
        else:
            return False

    def create_players(self, name: list):
        """Создает список игроков"""
        random.shuffle(name)
        for i in range(len(name)):
            self.gamers.append(Player(name[i], i))
    
    def next_round(self):
        """Передает право первого хода следующему игроку"""
        b = self.gamers[1:]
        b.append(self.gamers[0])
        self.gamers = b

    def roll_dices(self):
        """Обновляет список граней брошенных кубиков.
        Возвращает список [путь_к_картинке_стороны_кубика str, значение_течения_вресени int]"""
        a = []
        for_roll_dices = []
        d = self.data[self.cal.get_id_season()][1]
        for k in d.keys():
            a.append(k)
        random.shuffle(a)
        for i in a:
            side = random.choice(self.data[self.cal.get_id_season()][1][i])
            file_name = f'{self.data[self.cal.get_id_season()][0]}_{i}_{side[0]}.png'
            path_img_side = Path(self.p_img, file_name)
            for_roll_dices.append([str(path_img_side), side[1]])
        self.dices = for_roll_dices

    def id_season_to_season(self):
        """Возвращает название сезона на русском  по id сезона"""
        a = ['зима', 'весна', 'лето', 'осень']
        return a[self.cal.get_id_season()]

    def season_color(self):
        """Возвращает значение цвета в формате PySimpleGUI по id сезона"""
        a = ['LightSkyBlue1', 'PaleGreen1', 'khaki', 'salmon']
        return a[self.cal.get_id_season()]

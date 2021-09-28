import json
import random
from pathlib import Path
from Player import Player


class Game:

    def __init__(self, num_gamers: int, path_setting: str = 'settings.json', path_image: str = 'img'):
        self.num_gamers = num_gamers
        self.day = 1
        self.name_season = ["Зимы", "Весны", "Лета", "Осени"]
        self.p_settings = path_setting
        self.p_img = path_image
        self.data = self.j()
        self.dices = []
        self.gamers = []

    def j(self):
        """Парсим настройки"""
        with open(self.p_settings, 'r', encoding='utf-8') as j:
            return json.load(j)

    def time(self, time):
        """Время. Изменяет количество дней"""
        self.day += time
        if self.day <= 0:
            self.day = 12 - self.day

    def get_year(self):
        """Время. Возвращает количество прошедших полных лет игры"""
        year = (self.day-1)//12+1
        return year

    def get_day_in_period(self, period):
        """Время. Возвращает количество прошедших дней в текущем году"""
        day = self.day - ((self.day-1)//period)*period
        return day

    def get_id_season(self):
        """Время. Возвращает ID сезона"""
        day = self.get_day_in_period(12)
        season_id = (day - 1)//3
        return season_id

    def text_time(self):
        """Время. Возвращает дату игры в текстовом формате"""
        text = f'Идет {self.get_year()} год, {self.get_day_in_period(3)} месяц {self.name_season[self.get_id_season()]}'
        return text

    def time_end(self):
        """Время. Проверяет окончание третьего года игры"""
        if self.get_year() == 4:
            return True
        else:
            return False

    def create_players(self, name: list):
        """Принимает список имен и создает игроков.
        Создает список игроков [Имя, порядковый_номер] в случайном порядке"""
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
        d = self.data[self.get_id_season()][1]
        for k in d.keys():
            a.append(k)
        random.shuffle(a)
        for i in a:
            side = random.choice(self.data[self.get_id_season()][1][i])
            file_name = f'{self.data[self.get_id_season()][0]}_{i}_{side[0]}.png'
            path_img_side = Path(self.p_img, file_name)
            for_roll_dices.append([str(path_img_side), side[1]])
        self.dices = for_roll_dices

    def season_color(self):
        """Возвращает значение цвета в формате PySimpleGUI по id сезона"""
        a = ['LightSkyBlue1', 'PaleGreen1', 'khaki', 'salmon']
        return a[self.get_id_season()]

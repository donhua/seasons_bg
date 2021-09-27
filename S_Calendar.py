class S_Calendar:
    """Больше не используется. Удалить."""

    def __init__(self, nam_day: int = 1):
        self.day = nam_day

    def time(self, time):
        self.day += time
        return self.day

    def get_year(self):
        year = (self.day-1)//12+1
        return year

    def get_day_in_year(self):
        day = self.day - ((self.day-1)//12)*12
        return day

    def get_id_season(self):
        day = self.get_day_in_year()
        season_id = (day - 1)//3
        return season_id

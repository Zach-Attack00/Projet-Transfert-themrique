class Horloge:
    #Gestion du temps (temps, incérmentation de temps, obtenir valeur temps précédent, obtenir valeur temps actuel et setter un temps)
    def __init__(self):
        self.time = 0
        self.dt = 0.1

    def next_time(self):
        self.time += self.dt

    def get_previous_time(self):
        return self.time - self.dt

    def get_time(self):
        return self.time

    def set_time(self, t):
        self.time = t



    
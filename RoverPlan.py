

class RoverPlan:

    def __init__(self, start, commands):
        self.start = start
        self.commands = commands

    @property
    def start_x(self):
        return self.start[0]

    @property
    def start_y(self):
        return self.start[1]

    @property
    def start_d(self):
        return self.start[2]

    @property
    def commands(self):
        return self.commands

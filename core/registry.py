class CommandRegistry:
    def __init__(self):
        self.commands = {}

    def register(self, name, func):
        self.commands[name] = func

    def get_commands(self):
        return self.commands

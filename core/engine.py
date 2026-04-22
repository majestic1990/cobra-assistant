class Engine:
    def __init__(self):
        self.commands = {}

    def register_command(self, name, func):
        self.commands[name] = func

    def execute(self, command):
        if command in self.commands:
            return self.commands[command]()
        else:
            return f"Comando no reconocido: {command}"

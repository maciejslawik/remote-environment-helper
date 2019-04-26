class Completer:

    def __init__(self, commands):
        self.commands = commands

    def complete(self, text, state):
        options = [i for i in self.commands if i.startswith(text)]
        try:
            return options[state]
        except IndexError:
            return None

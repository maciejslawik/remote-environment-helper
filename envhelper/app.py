import readline
import sys
from envhelper.tools.autocompletion import Completer
from envhelper.actions.ssh import Ssh
from envhelper.actions.info import Info
from envhelper.actions.download import Download
from envhelper.actions.upload import Upload
from envhelper.tools.assistant import Assistant


class App:

    def __init__(self):
        self.__commands = {
            'ssh': self.__ssh,
            'info': self.__info,
            'download': self.__download,
            'upload': self.__upload
        }
        self.__assistant = Assistant()

    def start(self):
        try:
            action = self.__get_action()
            self.__commands[action]()
        except (KeyboardInterrupt, SystemExit, EOFError):
            pass
        except KeyError:
            self.__assistant.speak("Ups, you cannot do that...")

    def __get_action(self):
        try:
            action = sys.argv[1]
        except IndexError:
            self.__greet()
            completer = Completer(self.__get_commands().keys())
            readline.parse_and_bind("tab: complete")
            readline.set_completer(completer.complete)
            action = input("You> ")
        return action

    def __greet(self):
        self.__assistant.greet()
        self.__assistant.list_options(self.__get_commands().items())
        self.__assistant.speak("What can I do for you?")

    def __get_commands(self):
        commands = dict()
        commands.update(self.__commands)
        return commands

    def __ssh(self):
        action = Ssh()
        action.run()

    def __info(self):
        action = Info()
        action.run()

    def __download(self):
        action = Download()
        action.run()

    def __upload(self):
        action = Upload()
        action.run()

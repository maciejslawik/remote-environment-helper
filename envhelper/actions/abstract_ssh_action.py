from abc import abstractmethod
import readline
import sys
from envhelper.actions.action_interface import ActionInterface
from envhelper.tools.autocompletion import Completer
from envhelper.tools.assistant import Assistant
from envhelper.tools.access_data_provider import AccessDataProvider


class AbstractSshAction(ActionInterface):

    def __init__(self):
        self._data_provider = AccessDataProvider()
        self._assistant = Assistant()
        self._projects = self._data_provider.get_projects()
        self._environments = {}

    @abstractmethod
    def run(self):
        pass

    def _read_access_data(self):
        project = self.__read_project()
        self._environments = self._data_provider.get_environments(project)
        environment = self.__read_environment(project)
        readline.set_completer()
        return self._data_provider.get_access_data(project, environment)

    def _print_additional_info(self, access_data):
        if access_data.get_additional() != '':
            self._assistant.speak("Additional info: %s" % access_data.get_additional())

    def __read_project(self):
        try:
            project = sys.argv[2]
            if project in self._projects:
                return project
        except IndexError:
            pass
        while True:
            self._assistant.list_options(self._projects.items())
            self._assistant.speak("Which project is in your interest?")
            completer = Completer(self._projects.keys())
            readline.parse_and_bind("tab: complete")
            readline.set_completer(completer.complete)
            project = input("You> ")
            if project in self._projects:
                return project

    def __read_environment(self, project):
        try:
            environment = sys.argv[3]
            if environment in self._environments:
                return environment
        except IndexError:
            pass
        while True:
            self._assistant.list_options(self._environments.items())
            self._assistant.speak("And which environment of %s did you have in mind?" % project)
            completer = Completer(self._environments.keys())
            readline.parse_and_bind("tab: complete")
            readline.set_completer(completer.complete)
            environment = input("You> ")
            if environment in self._environments:
                return environment

import os
from envhelper.actions.abstract_ssh_action import AbstractSshAction
from envhelper.tools.path_reader import PathReader


class Upload(AbstractSshAction):

    def __init__(self):
        super().__init__()
        self._source_file = ''
        self._target_file = ''

    def run(self):
        access_data = self._read_access_data()
        self.__read_file_paths()
        self._print_additional_info(access_data)
        self._assistant.say_goodbye()
        self.__exec_scp(access_data)

    def __read_file_paths(self):
        source_file_found = False
        while not source_file_found:
            self._assistant.speak("Give me the path of the file to upload.")
            self.__source_file = PathReader.read_path()
            if not os.path.isfile(self.__source_file):
                self._assistant.speak("I couldn't find the file. Are you sure the path is correct?")
                continue
            source_file_found = True
            self._assistant.speak("Now give me the target path (on the server).")
            self.__target_file = input("You> ")

    def __exec_scp(self, access_data):
        os.system("scp -P %s %s %s@%s:%s" % (
            access_data.get_port(),
            self.__source_file,
            access_data.get_user(),
            access_data.get_ip(),
            self.__target_file
        ))

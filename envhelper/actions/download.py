import os
from envhelper.actions.abstract_ssh_action import AbstractSshAction
from envhelper.tools.path_reader import PathReader


class Download(AbstractSshAction):

    def __init__(self):
        super().__init__()
        self.__source_file = ''
        self.__target_file = ''

    def run(self):
        access_data = self._read_access_data()
        self.__read_file_paths()
        self._print_additional_info(access_data)
        self._assistant.say_goodbye()
        self.__exec_scp(access_data)

    def __read_file_paths(self):
        self._assistant.speak("Give me the path of the file to download (on the remote server).")
        self.__source_file = input("You> ")
        self._assistant.speak("Now give me the local path for the downloaded file.")
        self.__target_file = PathReader.read_path()

    def __exec_scp(self, access_data):
        os.system("scp -P %s %s@%s:%s %s" % (
            access_data.get_port(),
            access_data.get_user(),
            access_data.get_ip(),
            self.__source_file,
            self.__target_file
        ))

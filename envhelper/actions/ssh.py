import os
from envhelper.actions.abstract_ssh_action import AbstractSshAction


class Ssh(AbstractSshAction):

    def run(self):
        access_data = self._read_access_data()
        self._print_additional_info(access_data)
        self._assistant.say_goodbye()
        self.__exec_ssh(access_data)

    def __exec_ssh(self, access_data):
        os.system("ssh %s@%s -p  %s" % (access_data.get_user(), access_data.get_ip(), access_data.get_port()))

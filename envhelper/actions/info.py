from envhelper.actions.abstract_ssh_action import AbstractSshAction


class Info(AbstractSshAction):

    def run(self):
        access_data = self._read_access_data()
        self.__print_info(access_data)
        self._assistant.say_goodbye()

    def __print_info(self, access_data):
        self._assistant.speak(''
                            'There you go: \n'
                            '* Project: %s\n'
                            '* Environment: %s\n'
                            '* SSH user: %s\n'
                            '* IP: %s\n'
                            '* SSH port: %s\n'
                            '* Additional info: %s\n'
                            % (access_data.get_project(),
                               access_data.get_environment(),
                               access_data.get_user(),
                               access_data.get_ip(),
                               access_data.get_port(),
                               access_data.get_additional())
                            )

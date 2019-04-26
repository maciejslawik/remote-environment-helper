class AccessData:
    def __init__(self, project, environment, user, ip, port, additional):
        self._project = project
        self._environment = environment
        self._user = user
        self._ip = ip
        self._port = port
        self._additional = additional

    def get_project(self):
        return self._project

    def get_environment(self):
        return self._environment

    def get_user(self):
        return self._user

    def get_ip(self):
        return self._ip

    def get_port(self):
        return self._port

    def get_additional(self):
        return self._additional

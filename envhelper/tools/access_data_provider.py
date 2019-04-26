from envhelper.tools.csv_access_data_reader import CsvAccessDataReader


class AccessDataProvider:

    def __init__(self):
        data_reader = CsvAccessDataReader()
        self.__access_data = data_reader.read_access_data()

    def get_projects(self):
        return {access_datum.get_project(): access_datum.get_project() for access_datum in self.__access_data}

    def get_environments(self, project):
        return {access_datum.get_environment(): access_datum.get_environment() for access_datum in self.__access_data if
                access_datum.get_project() == project}

    def get_access_data(self, project, environment):
        for access_datum in self.__access_data:
            if access_datum.get_project() == project and access_datum.get_environment() == environment:
                return access_datum

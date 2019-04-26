from envhelper.tools.access_data_reader_interface import AccessDataReaderInterface
from envhelper.entity.access_data import AccessData
import csv
import os


class CsvAccessDataReader(AccessDataReaderInterface):

    def read_access_data(self):
        path = os.path.dirname(os.path.realpath(__file__)) + '/../data/access.csv'
        with open(path, mode='r') as access_data:
            reader = csv.reader(access_data)
            data = []
            for row in reader:
                data_object = AccessData(row[0], row[1], row[2], row[3], row[4], row[5])
                data.append(data_object)
        return data

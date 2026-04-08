import json


class IO_helper:
    @staticmethod
    def save(data, filename):
        with open(filename, 'w') as f:
            json.dump(data, f)
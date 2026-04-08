import json


class IO_helper:
    @staticmethod
    def save(data, filename):
        with open(filename, 'w') as f:
            json.dump(data, f)
    
    @staticmethod
    def load(filename):
        with open(filename, 'r') as f:
            return json.load(f)
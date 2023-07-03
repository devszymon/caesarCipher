import json


class ReadJson:
    @staticmethod
    def read_json(file_name: str) -> dict:
        with open(file_name, "r") as json_file:
            data = json.load(json_file)

        return data

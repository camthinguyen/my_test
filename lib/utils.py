import json


class Utils:

    # Convert response data to json
    @classmethod
    def get_data_in_json(self, response):
        raw_data = response.read().decode('utf-8')
        return json.loads(raw_data)

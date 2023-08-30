import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url
        
    def get_response_body(self):
        response = requests.get(self.url)
        return response.content

    def load_json(self):
        program_list = []
        response_content = self.get_response_body()
        response = json.loads(response_content)
        for program in response:
            program_list.append(program)

        return program_list
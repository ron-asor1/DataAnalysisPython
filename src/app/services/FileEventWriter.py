import json

class FileEventWriter:
    def __init__(self, file_path):
        self.file_path = file_path

    def write_event(self, event):
        with open(self.file_path, 'a') as file:
            file.write(str(event) + '\n')

    def write_event_json(self, event):
        with open(self.file_path, 'a') as file:
            json_event = json.dumps(event.__dict__)
            file.write(json_event + '\n')
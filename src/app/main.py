# main.py
from app.services.EventGenerator import EventGenerator
from app.services.FileEventWriter import FileEventWriter
from app.services.LogConveter import LogConverter
from app.services.EventManagerDB import EventManagerDB
import datetime
import os
from dotenv import load_dotenv

load_dotenv()

class EventManager:
    def __init__(self):
        self.now = datetime.datetime.now()
        self.generator = EventGenerator()
        self.db_manager = EventManagerDB()
        self.input_file = os.getenv("EVENT_LOG_PATH")+"events_" + str(self.now)+".log"
        self.output_file = os.getenv("EVENT_JSON_PATH")+"event_json_"+str(self.now)+".json"
        self.file_writer = FileEventWriter(self.input_file)

    def generate_pageview(self):
        event = self.generator.generate_pageview_event()
        self.db_manager.inset_event(event)
        print(event)
        self.file_writer.write_event(event)
        convert_log_to_json(self)
        return event

    def generate_purchase(self):
        event = self.generator.generate_purchase_event()
        self.db_manager.inset_event(event)
        print(event)
        self.file_writer.write_event(event)
        convert_log_to_json(self)
        return event

def convert_log_to_json(self):
    converter = LogConverter(self.input_file, self.output_file)
    converter.convert()
    print("Conversion completed.")

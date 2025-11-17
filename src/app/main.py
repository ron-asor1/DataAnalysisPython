from app.services.EventGenerator import EventGenerator
from app.services.FileEventWriter import FileEventWriter
from app.services.LogConveter import LogConverter
import datetime
import os
from dotenv import load_dotenv

load_dotenv()
now = datetime.datetime.now()
generator = EventGenerator()
inputFilePath = os.getenv("EVENT_LOG_PATH")+"events_" + str(now)+ ".log"
outputFilePath = os.getenv("EVENT_JSON_PATH")+"event_json_"+str(now)+".json"
fileEventWriter = FileEventWriter(inputFilePath)
iteration = int(os.getenv("ITERATION_COUNT"))
a = 0
b = 0

class EventManager:
    while a < iteration:
        pv_evenet = generator.generate_pageview_event()
        print(pv_evenet)
        fileEventWriter.write_event(pv_evenet)
        a+=1

    while b < iteration:
        purchaseEvent = generator.generate_purchase_event()
        print(purchaseEvent)
        fileEventWriter.write_event(purchaseEvent)
        b+=1

    converter = LogConverter(inputFilePath, outputFilePath)
    converter.convert()
    print("Conversion completed.")



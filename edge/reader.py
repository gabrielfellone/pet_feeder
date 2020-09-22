import json
import time
from connection import Connection

class Reader:
    def __init__(self, port, baud):
        self.data = ''
        self.port = port
        self.baud = baud
        self.conn = Connection(port=port, baud=baud).connect()

    def getData(self):
        if(self.conn != 0):
            self.data = str(self.conn.readline().decode('utf-8').rstrip())
            return self.buildPayload()
        else:
            time.sleep(10)
            self.conn = Connection(port=self.port, baud=self.baud).connect()
            self.getData()

    def buildPayload(self):
        payload = {}
        payload['sensor'] = 'pet_01'
        payload['presence'] = True if self.data == '1' else False

        return json.dumps(payload)

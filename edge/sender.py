import time
import logging
import datetime
from connection import Connection

class Sender:
    def __init__(self, port, baud, datetime):
        self.port = port
        self.baud = baud
        self.conn = Connection(port=port, baud=baud).connect()
        self.datetime = datetime

    def alimentar(self):
        logging.info('Verificando se porta esta conectada: %s', self.conn)
        if(self.conn != 0):
            if (datetime.datetime.now() >= self.datetime):
                logging.info('Tempo maior ou igual ao de agora')
                self.conn.write('open'.encode())
                self.datetime = datetime.datetime.now() + datetime.timedelta(microseconds=60)
                logging.info('Setando um intervalo de: %s', self.datatime)
        else:
            logging.error('Porta desconectada timer de 30secs para proxima tentativa')
            time.sleep(30)
            self.conn = Connection(port=self.port, baud=self.baud).connect()
            self.alimentar

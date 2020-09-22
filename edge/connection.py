import serial

class Connection:
    def __init__(self, port='/dev/ttyUSB0', baud=9600):
        self.port = port
        self.baud = baud
        self.data = ''

    def connect(self):
        try:
            conn = serial.Serial(self.port, self.baud)
            print('Conectado com sucesso.\n')
            return conn
        except:
            print('Sem conexão na porta ' + str(self.port) + '.\n')
            return 0

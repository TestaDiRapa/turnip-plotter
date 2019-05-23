import re
import serial


def initialize_serial(port):
    """
    Check if the device is available and if the data are correctly formatted
    :param port: the port to listen
    :return: the number of values to plot
    """
    with serial.Serial(port) as device:
        for i in range(100):
            line = device.readline().decode('utf-8')
            if re.search(r'^-?\d+(\.\d+)?(\t-?\d+(\.\d+)?)*\r?\n$', line):
                break
        else:
            raise Exception("Wrong data format!")

        return len(line.split('\t'))


def read_from_serial(buffers):
    with serial.Serial('/dev/ttyACM0') as device:
        while not re.search(r'^-?\d+(\.\d+)?(\t-?\d+(\.\d+)?)+\r?\n$', device.readline().decode('utf-8')):
            pass
        while True:
            line = re.sub('\r', '', re.sub('\n', '', device.readline().decode('utf-8')))
            try:
                values = [eval(x) for x in line.split('\t')]
                for j in range(len(buffers)):
                    buffers[j].pop(0)
                    buffers[j].append(values[j])
            except ValueError:
                pass

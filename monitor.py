import matplotlib.pyplot as plt
import matplotlib.animation as animation
import re
import serial
import threading

length = 100
buffers = []
variables = 3
for i in range(variables):
    buffers.append([0 for i in range(length)])
current = 0
fig = plt.figure()
plt.ylim(-1000, 1000)
ax = fig.add_subplot(3, 1, 1)
ay = fig.add_subplot(3, 1, 2)
az = fig.add_subplot(3, 1, 3)


def read_from_serial():
    global buffers
    with serial.Serial('/dev/ttyACM0') as device:
        device.readline()
        device.readline()
        while True:
            line = re.sub('\r', '', re.sub('\n', '', device.readline().decode('utf-8')))
            values = [int(x) for x in line.split('\t')]
            for j in range(3):
                buffers[j].pop(0)
                buffers[j].append(values[j])


def real_time_plot(i):
    global buffers
    ax.clear()
    az.clear()
    ay.clear()
    ax.plot(buffers[0], color='red')
    ay.plot(buffers[1], color='blue')
    az.plot(buffers[2], color='green')


threading.Thread(target=read_from_serial).start()
a = animation.FuncAnimation(fig, real_time_plot, interval=10)
plt.show()



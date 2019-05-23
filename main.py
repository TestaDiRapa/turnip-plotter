from threading import Thread
import device
import matplotlib.animation as animation
import matplotlib.pyplot as plt


colors = ['red', 'green', 'blue', 'black']


def real_time_plot(fig, buffers, sub_plots):
    for i in range(len(buffers)):
        sub_plots[i].clear()
        sub_plots[i].plot(buffers[i], color=colors[i % len(colors)])


def main():

    # Reads from the user the serial port to read from
    port = input("Insert the serial directory [/dev/ttyACM0]: ")
    if len(port) == 0:
        port = "/dev/ttyACM0"

    length = input("Specify the x-axis length [100]: ")
    try:
        length = int(length)
        if length < 0:
            length = 100
    except ValueError:
        length = 100

    num_values = device.initialize_serial(port)

    buffers = []
    for i in range(num_values):
        buffers.append([0 for i in range(length)])

    fig = plt.figure()

    sub_plots = []
    for i in range(num_values):
        sub_plots.append(fig.add_subplot(num_values+1, 1, i+1))

    Thread(target=device.read_from_serial, args=(buffers,)).start()
    a = animation.FuncAnimation(fig, real_time_plot, fargs=(buffers, sub_plots), interval=10)
    plt.show()


if __name__ == "__main__":
    main()

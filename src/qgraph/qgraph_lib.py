# Module for generating quick graphs
import matplotlib.pyplot as plt


def txt_to_nums(lines):
    return [float(line) for line in lines]


def graph(series, title=None, style='line'):
    if len(series) == 0:
        raise Exception("Must have at least one series of data")

    # tkinter specific code
    mgr = plt.get_current_fig_manager()
    mgr.window.geometry("+50+50")

    count = sum([len(s) for s in series])
    label = f"Graph of {count} numbers in {len(series)} series"
    if title is not None:
        label = title + ' - ' + label

    if style == 'line':
        for s in series:
            plt.plot(s)
    elif style == 'bar':
        for s in series:
            plt.bar(range(len(s)), s)
    elif style == 'pie':
        if len(series) > 1:
            raise Exception('pie graph can only support one series')
        plt.pie(series[0])
    elif style == 'histogram':
        for s in series:
            plt.hist(s, bins=10)

    plt.title(label)
    plt.show()

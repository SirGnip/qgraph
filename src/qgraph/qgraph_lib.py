# Module for generating quick graphs
import matplotlib.pyplot as plt


def txt_to_nums(lines):
    return [float(line) for line in lines]


def graph(nums1, title=None, type='bar'):
    # tkinter specific code
    mgr = plt.get_current_fig_manager()
    mgr.window.geometry("+50+50")

    label = f"Graph of {len(nums1)} numbers"
    if title is not None:
        label = title + ' - ' + label

    if type == 'bar':
        plt.plot(nums1)
    elif type == 'histogram':
        plt.hist(nums1, bins=10)

    plt.title(label)
    plt.show()

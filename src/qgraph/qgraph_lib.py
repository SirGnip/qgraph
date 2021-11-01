# Module for generating quick graphs
import matplotlib.pyplot as plt


def txt_to_nums(lines):
    return [float(line) for line in lines]


def graph(nums1, title=None, style='line'):
    # tkinter specific code
    mgr = plt.get_current_fig_manager()
    mgr.window.geometry("+50+50")

    label = f"Graph of {len(nums1)} numbers"
    if title is not None:
        label = title + ' - ' + label

    if style == 'line':
        plt.plot(nums1)
    elif style == 'bar':
        plt.bar(range(len(nums1)), nums1)
    elif style == 'pie':
        plt.pie(nums1)
    elif style == 'histogram':
        plt.hist(nums1, bins=10)

    plt.title(label)
    plt.show()

# Module for generating quick graphs
import matplotlib.pyplot as plt


def txt_to_nums(lines):
    return [float(line) for line in lines]


def graph(nums1, title=None):
    plt.plot(nums1)
    label = f"Graph of {len(nums1)} numbers"
    if title is not None:
        label = title + ' - ' + label
    plt.title(label)
    plt.show()

from qgraph.qgraph_lib import graph

nums = (1, 3, 2, 9, 4)
nums2 = (1, 2, 7, 5, 3, 5, 5, 6, 2, 6, 5, 6, 5, 4, 5, 10, 5, 4, 4, 6, 4)


def test_default():
    graph(nums)


def test_bar():
    graph(nums, style='bar')


def test_line():
    graph(nums, style='line')


def test_pie():
    graph(nums, style='pie')


def test_histo():
    graph(nums2, style='histogram')

from qgraph.qgraph_lib import graph


def test_basic():
    graph((1, 3, 2, 9, 4))


def test_basic2():
    graph((2, 8, 2, 3, 9, -3, 15.5))


def test_histo():
    graph((1, 2, 7, 5, 3, 5, 5, 6, 2, 6, 5, 6, 5, 4, 5, 10, 5, 4, 4, 6, 4), type='histogram')

from src.pre_built.counter import count_ocurrences


def test_counter():
    pathfile = "data/jobs.csv"
    assert count_ocurrences(pathfile, "Python") == 1639
    assert count_ocurrences(pathfile, "Javascript") == 122

from src.pre_built.counter import count_ocurrences


def test_count_ocurrences():
    pathfile = "data/jobs.csv"
    assert count_ocurrences(pathfile, "test") == 2687

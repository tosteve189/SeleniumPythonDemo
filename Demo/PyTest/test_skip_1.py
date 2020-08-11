# pytest *.py -v (with verbal)
# pytest *.py -v -rxs (Specify reasons)
# pytest *.py -k demo_3  (run the test with partial string captured)


import pytest


@pytest.mark.skip(reason="Not included in this build")
def test_demo_1():
    assert True


def test_demo_2():
    assert True


def test_demo_3():
    assert True

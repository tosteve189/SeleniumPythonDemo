# pytest *.py -v (with verbal)
# pytest *.py -v -rxs (Specify reasons)
# pytest *.py -k demo_3  (run the test with partial string captured)
# import sys to perform conditional skip
# Use pytest.mark to distinguish windows or mac
# Use pytest test_skip_os.py -m windows -v


import pytest
import sys


@pytest.mark.windows
def test_windows_1():
    assert True


@pytest.mark.windows
def test_windows_2():
    assert True


@pytest.mark.mac
def test_mac_1():
    assert True


@pytest.mark.mac
def test_mac_2():
    assert True


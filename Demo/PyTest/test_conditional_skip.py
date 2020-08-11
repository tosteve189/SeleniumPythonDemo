# pytest *.py -v (with verbal)
# pytest *.py -v -rxs (Specify reasons)
# pytest *.py -k demo_3  (run the test with partial string captured)
# import sys to perform conditional skip

import pytest
import sys


@pytest.mark.skip(reason="Not included in this build")
def test_demo_1():
    assert True


@pytest.mark.skip(sys.version_info < (3, 6),
                  reason="requires python 3.6 or higher")
def test_demo_2():
    assert True


def test_demo_3():
    assert True

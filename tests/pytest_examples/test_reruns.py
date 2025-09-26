import pytest
import random

PLATFORM = "Windows"


@pytest.mark.flaky(reruns=3, reruns_delay=2)
def test_rerurns():
    assert False


@pytest.mark.flaky(reruns=3, reruns_delay=2)
class TestReruns:
    def test_rerun1(self):
        assert random.choice([True, False])

    def test_rerun2(self):
        assert random.choice([True, False])


@pytest.mark.flaky(reruns=3, condition=(PLATFORM == "Windows"))
def test_rerun_with_condition():
    assert random.choice([True, False])

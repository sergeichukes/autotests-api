import pytest


@pytest.mark.flaky(reruns=3, reruns_delay=2)
def test_rerurns():
    assert False

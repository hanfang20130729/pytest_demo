import pytest


def hello_world(*args, **kwargs):
    return "Hello World"


@pytest.mark.my_marker.with_args(hello_world)
def test_with_args():
    pass

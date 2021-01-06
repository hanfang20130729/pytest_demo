# -*- coding:utf-8 -*-

import pytest


class TestClassXfail:
    @pytest.mark.xfail(reason="---xfail---")
    def test_1(self):
        assert 1 == 0

    def test_han_2(self):
        print("test_2")

    def test_3(self):
        print("test_3")


@pytest.mark.xfail(reason="---xfail---")
class TestClassXfail1:
    def test_1(self):
        assert 1 == 0

    def test_han_2(self):
        print("test_2")


@pytest.mark.xfail(reason="---xfail---")
def test_xfail():
    assert 1 == 2


@pytest.mark.xfail(reason="---xfail---")
def test_xfail1():
    assert 1/0


@pytest.mark.parametrize(
    ("t"),
    [
        pytest.param(1, marks=pytest.mark.xfail)
    ]
)
def test_xfail2(t):
    assert t == 2

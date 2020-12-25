# -*- coding:utf-8 -*-
import pytest


def func(x):
    return x + 1


def test_answer():
    assert func(3) == 5


def f():
    raise SystemExit(1)


# pytest如何主动异常
def test_mytest():
    with pytest.raises(SystemExit):
        f()


class TestClass1:
    def test_han_1(self):
        print("test_1")

    def test_2(self):
        print("test_2")

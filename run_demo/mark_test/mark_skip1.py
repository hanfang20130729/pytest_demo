# -*- coding:utf-8 -*-

import pytest

# 三种方式作用阈都是整个模块哦
# pytest.skip("---skip---", allow_module_level=True)
# pytestmark = pytest.mark.skip
pytestmark = pytest.mark.skipif(1 == 1, reason="---skipif---")


def test_skip():
    assert 0 > 3


def test_skip1():
    assert 1 == 0


def test_skip2():
    print("skip")
    assert 1 == 0


class TestClassSkip:
    def test_skip1(self):
        print("skip1")

    def test_skip2(self):
        print("skip2")

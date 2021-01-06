# -*- coding:utf-8 -*-

import pytest


# import sys


# @pytest.mark.skipif(sys.platform == "win32",
#                     reason="---skipif---")
# 'sys.platform == "win32"'这样不用import sys 也没有问题
@pytest.mark.skipif('sys.platform == "win32"',
                    reason="---skipif---")
def test_func_skip():
    print("skip")


@pytest.mark.skip(reason="---skip---")
def test_func_skipif():
    print("skipif")


def test_func_inner_skip():
    print("skip")
    pytest.skip("---skip---")
    assert 1 == 0


def test_func_inner_skip1():
    print("skip")
    pytest.importorskip(modname="pymysql", minversion="3.5.6", reason="---skip---")
    assert 1 == 0

# 这样的用法会让整个模块的用例计算不上---不知道为啥，可能是一个bug，有时间在gitbug上提供下
# @pytest.importorskip(modname="pymysql", minversion="3.5.6", reason="---skip---")
# def test_func_inner_skip2():
#     print("skip")
#     assert 1 == 0


class TestClassSkip1:
    @pytest.mark.skipif(1 > 0, reason="---skipif---")
    def test_class_skipif(self):
        print("skip1")

    @pytest.mark.skip(reason="---skip---")
    def test_class_skip(self):
        print("skip2")


@pytest.skip("---skip---")
class TestClassSkip2:
    def test_skip1(self):
        print("skip1")

    def test_skip2(self):
        print("skip2")


@pytest.mark.skipif(reason="---skipif---")
class TestClassSkip3:
    def test_skip1(self):
        print("skip1")

    def test_skip2(self):
        print("skip2")


class TestClassSkip4:
    def test_class_inner_skip(self):
        print("skip3")
        pytest.skip("---skip---")
        assert 2 == 4

# -*- coding:utf-8 -*-

import pytest


def test_skip1():
    print("skip1")


@pytest.mark.skip(reason="跳过这个方法")
def test_skip2():
    print("skip2")


class TestSkip1:
    def test_skip1(self):
        print("skip1")

    @pytest.mark.skip(reason="跳过这个类方法")
    def test_skip2(self):
        print("skip2")


@pytest.mark.skip(reason="跳过这个类")
class TestSkip2:
    def test_skip1(self):
        print("skip1")

    def test_skip2(self):
        print("skip2")


class TestSkip3:
    def test_skip1(self):
        print("skip1")
        print("!!!!!")
        pytest.mark.skip(reason="用例里面执行到哪里就跳过")

    def test_skip2(self):
        print("skip2")

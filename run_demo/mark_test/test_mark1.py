# -*- coding:utf-8 -*-

import pytest


class TestClassMark:
    @pytest.mark.me
    def test_1(self):
        print("test_1")

    def test_han_2(self):
        print("test_2")

    def test_3(self):
        print("test_3")

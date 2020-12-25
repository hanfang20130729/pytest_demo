# -*- coding:utf-8 -*-

import pytest


class TestClassMark1:
    @pytest.mark.me
    def test_4(self):
        print("test_4")

    def test_5(self):
        print("test_25")

    def test_6(self):
        print("test_6")
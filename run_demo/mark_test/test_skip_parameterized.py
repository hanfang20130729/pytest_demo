# -*- coding:utf-8 -*-

import pytest
import sys


@pytest.mark.parametrize(
    ("n", "expected"),
    [
        pytest.param(1, 2, marks=pytest.mark.skip(reason="---skip---")),
        pytest.param(1, 3, marks=pytest.mark.me),
        pytest.param(2, 3, marks=pytest.mark.skipif(sys.platform == "win32",
                                                    reason="---skipif---"))
    ]
)
def test_skip_parametrize(n, expected):
    assert n + 1 == expected


@pytest.mark.skip("---skip---")
@pytest.mark.parametrize(
    ("test_input", "expected"),
    [
        ("3+5", 8),
        ("2+4", 6)
    ]
)
def test_eval(test_input, expected):
    assert eval(test_input) == expected

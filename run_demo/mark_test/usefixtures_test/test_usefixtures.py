import os
import pytest


@pytest.mark.usefixtures("cleandir")
class TestDirectoryInit:
    def test_cwd_starts_empty(self):
        print(os.listdir(os.getcwd()))
        with open("myfile", "w") as f:
            f.write("hello")
        print(os.listdir(os.getcwd()))

    def test_cwd_again_starts_empty(self):
        print(os.listdir(os.getcwd()))
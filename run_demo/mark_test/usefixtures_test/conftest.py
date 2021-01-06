import os
import shutil
import tempfile

import pytest


@pytest.fixture
def cleandir():
    print("cleandir")
    # if os.path.isfile(
    #     "myfile"
    # ):
    #     os.remove("myfile")

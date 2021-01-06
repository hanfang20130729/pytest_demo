import pytest
import sys

# def pytest_addoption(parser):
#     parser.addoption(
#         "-E",
#         action="store",
#         metavar="NAME",
#         help="only run tests matching the environment NAME.",
#     )
#
#
def pytest_configure(config):
    # register an additional marker
    config.addinivalue_line("markers", "env(name): mark test to run only on named environment")
    config.addinivalue_line("markers", "win32: win32环境")
    config.addinivalue_line("markers", "linux: linux环境")
    config.addinivalue_line("markers", "darwin: darwin环境")
#
#
# def pytest_runtest_setup(item):
#     envnames = [mark.args[0] for mark in item.iter_markers(name="env")]
#     if envnames:
#         if item.config.getoption("-E") not in envnames:
#             pytest.skip("test requires env in {!r}".format(envnames))

# def pytest_runtest_setup(item):
#     for marker in item.iter_markers(name="my_marker"):
#         print(marker)
#         sys.stdout.flush()


# def pytest_runtest_setup(item):
#     for mark in item.iter_markers(name="glob"):
#         print("glob args={} kwargs={}".format(mark.args, mark.kwargs))
#         sys.stdout.flush()


ALL = set("darwin linux win32".split())
print(ALL)


def pytest_runtest_setup(item):
    print(item)
    print(mark.name for mark in item.iter_markers())
    supported_platforms = ALL.intersection(mark.name for mark in item.iter_markers())
    print(supported_platforms)
    plat = sys.platform
    print(plat)
    if supported_platforms and plat not in supported_platforms:
        pytest.skip("cannot run on platform {}".format(plat))








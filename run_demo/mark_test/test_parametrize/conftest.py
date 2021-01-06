# conftest中固定的方法，添加命令行自定义参数，这里添加--all的参数
def pytest_addoption(parser):
    parser.addoption("--all", action="store_true", help="run all combinations")


def pytest_generate_tests(metafunc):
    # metafunc.fixturenames获取的是测试用例的入参？？？
    if "param1" in metafunc.fixturenames:
        # metafunc.config.getoption获取命令行参数
        if metafunc.config.getoption("all"):
            end = 5
        else:
            end = 2
        metafunc.parametrize("param1", range(end))
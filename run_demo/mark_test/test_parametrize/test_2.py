# 是不是校验mysql，校验redis可以在这里面去看情况，默认不校验
# 利用命令行参数控制一些参数值，这里用命令行--all参数控制param1的取值范围


def test_compute(param1):
    assert param1 < 4
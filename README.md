# pytest_demo
study go go go
官方文档：https://docs.pytest.org/
1、安装环境
   （1）python3下新建虚拟环境：mkvirtualenv --python==C:\Python\Python37\python.exe my_pytest
   （2）安装pytest：pip install pytest
   （3）pip install pytest-cov # 计算pytest覆盖率，支持输出多种格式的测试报告
   （4）pip install pytest-randomly 测试顺序随机
   （5）pip install pytest-xdist  分布式测试
   （6）pip install pytest-instafail 错立即返回
   
2、用例执行方法：
    （1）运行一个python文件： pytest run_demo/test_funcname.py
    （2）运行一个python文件中一个测试用例方法：pytest run_demo/test_funcname.py::test_mytest
    （3）运行一个python文件中一个测试类下用例：pytest run_demo/test_funcname.py::TestClass1
    （4）运行一个python文件中一个测试类下某个用例：pytest run_demo/test_funcname.py::TestClass1::test_1  
    （5）运行一类测试用例：
         第一种：-k参数表示用例的名字中包含关键字内容
                 eg1：pytest -k TestClass1  运行了test_funcname.py和test_funcname2.py里面一共4个用例
                 eg2: pytest -k "han" -v    运行了包含han在没的用例
         第二种：mark功能--后面单独一个地方说
 3、mark功能
    （1） @pytest.mark.skip(reason=None)  标记用例方法、用例类不执行，跳过

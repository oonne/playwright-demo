import unittest

class TestExample(unittest.TestCase):
    def setUp(self):
        # 初始化代码
        pass

    def tearDown(self):
        # 清理代码
        pass

    def test_example(self):
        print('hello world')


if __name__ == '__main__':
    unittest.main()
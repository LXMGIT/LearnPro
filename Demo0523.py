# coding = utf-8
import unittest

from HTMLTestRunner.HTMLTestRunner import HTMLTestRunner


class unitDemo(unittest.TestCase):
    def setUp(self) -> None:
        print("set Up ...")
    def tearDown(self) -> None:
        print("tear Down ...")

    def test_case01(self):
        self.assertEqual(2,2,'值不相等')

    def test_case02(self):
        self.assertEqual(2,3,'值不相等')


if __name__ == '__main__':
#     unittest.main()
    suit = unittest.TestSuite()
    suit.addTest(unitDemo('test_case01'))
    suit.addTest(unitDemo('test_case02'))
#     unittest.TextTestRunner().run(suit)
    with open('report.html','w') as f:
        runner = HTMLTestRunner(stream = f,
                        title = 'reprot',
                        description = 'excute statuation',
                        verbosity = 2
                        )
        runner.run(suit)

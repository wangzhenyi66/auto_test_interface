import unittest
from unittestreport import TestRunner

from auto_test_interface.test_case.test_http_request import TestHttpRequest


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(TestHttpRequest('test_case_01'))
    runner = TestRunner(suite)
    runner.run()
    runner.send_email(host="smtp.qq.com",
                      port=465,
                      user="1665608695@qq.com",
                      password="wh157984632.",
                      to_addrs="3191526804@qq.com",
                      )


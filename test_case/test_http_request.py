import unittest
import pymysql.cursors
import logging
from auto_test_interface.common.http_request import HttpRequest

logging.basicConfig(level=logging.INFO)

con = pymysql.connect(
    host='localhost',
    user='root',
    password='root',
    db='guest',
)

cursor = con.cursor()
sql = 'select * from test_data'

cursor.execute(sql)
test_data = cursor.fetchall()
for i in test_data:
    print("*" * 30)
    print("ddt 分解传递出来的参数是：{0}".format(i))


class TestHttpRequest(unittest.TestCase):

    def test_case_01(self):
        """
        case12
        :return:
        """

        for data in test_data:
            url = data[3]
            params = data[4]
            method = data[2]
            #
            # res = HttpRequest(url, eval(params)).http_request(method)
            # logging.info("测试请求的url是{0}\n使用的参数为{1}\n使用的请求方法是{2}\n测试结果为{3}\n****************".format(url, params, method, res.json()))
            # # print("测试用例的执行结果是：{0}".format(res.json()))

    def tearDown(self) -> None:
        cursor.close()
        con.close()


if __name__ == '__main__':
    unittest.main()


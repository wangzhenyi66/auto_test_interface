import requests


class HttpRequest(object):
    # 创建初始化函数，每次请求都要提供 url param 两个必备参数
    def __init__(self, url, param):
        self.url = url
        self.param = param

    def http_request(self, method, cookie=None):
        if method.upper() == "GET":
            try:
                res = requests.get(self.url, self.param, cookies=cookie)
            except Exception as e:
                print("执行 get 请求报错，错误是{0}".format(e))
                res = "Error : get 请求报错{0}".format(e)

        elif method.upper() == "POST":
            try:
                res = requests.post(self.url, self.param, cookies=cookie)
            except Exception as e:
                print("执行 post 请求报错{0}".format(e))
                res = "Error : post 请求报错{0}".format(e)
        else:
            print("请求方式不对！")
            res = "Error : 请求方法不对，报错{0}".format(method)
        return res


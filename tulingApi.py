# -*- coding:utf-8 -*-
import json
import logging
import requests
from urllib import urlopen
from urllib import urlencode



class TulingAPI(object):


    def __init__(self):
        # API接口地址
        self.turing_url = 'http://openapi.tuling123.com/openapi/api/v2?'

    def get_turing_text(self,text):
        turing_url_data = {
            "perception": {
                "inputText": {
                    "text": text
                }
            },
            "userInfo": {
                "apiKey": "f71ceb0de7d84bffa71a34ee34fa40c7",
                "userId": "f71ceb0de7d84bffa71a34ee34fa40c7"
            }
        }
        # print("The things to Request is:",self.turing_url + urlencode(turing_url_data))

        # print("The result of Request is:",self.request)

        try:
            self.request = requests.post(self.turing_url, data=json.dumps(turing_url_data))
            # print("Type of the data from urlopen:",type(w_data))
            # print("The data from urlopen is:",w_data)
        except Exception,e:
             logging.error(e.message)
             raise KeyError("Server wouldn't respond (invalid key or quota has been maxed out)")
            # 其他情况断言提示服务相应次数已经达到上限

        response_text = self.request.text
        # print("Type of the response_text :",type(response_text))
        # print("response_text :",response_text)

        json_result = json.loads(response_text)
        # print("Type of the json_result :",type(json_result))
        return json.loads(response_text)['results'][0]['values']['text'].encode('utf-8')

if __name__ == '__main__':
    print("Now u can type in something & input q to quit")

    turing = TulingAPI()

    while True:
        msg = raw_input('\nMaster:')
        if msg == 'q':
            exit("u r quit the chat !")         # 设定输入q，退出聊天。
        else:
            turing_data = turing.get_turing_text(msg)
            print turing_data
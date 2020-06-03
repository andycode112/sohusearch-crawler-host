'''
@Author: your name
@Date: 2020-05-15 08:52:23
@LastEditTime: 2020-06-03 14:45:57
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \python\sohu-crawler\app.py
'''
#coding:utf-8
import os,flask,json
from server.serverinfoapi import serverinfo
from server.sohuapi import sohuapi
from server.Logger import Logger
# from flask import request,configparser
# from datetime import datetime
# import urllib
# from wsgiref.simple_server import make_server
log = Logger(name='sohusearchhost')

#create a service of the current python file　
app = flask.Flask(__name__)
app.register_blueprint(serverinfo)
app.register_blueprint(sohuapi)

@app.route('/',methods=['get'])
def health():
    ret={'code':200,'message':'the server is ok'}
    return json.dumps(ret,ensure_ascii=False)


# py -3 .\sohu-crawler\main.py
if __name__== '__main__':
    app.run(debug=True,port = 5000,host='0.0.0.0')
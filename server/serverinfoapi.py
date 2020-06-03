'''
@Author: your name
@Date: 2020-05-16 17:07:22
@LastEditTime: 2020-05-25 11:10:15
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \python\souhu-crawler\server\serverinfoapi.py
'''
from flask import Blueprint
import json,datetime

serverinfo = Blueprint('serverinfoapi', __name__)

@serverinfo.route('/serverdate',methods=['get'])
def serverdate():
    #username = request.values.get('name')
    ret={'code':200,'servertime':datetime.datetime.strftime(datetime.datetime.now(),'%Y-%m-%d %H:%M:%S')}
    return json.dumps(ret,ensure_ascii=False)

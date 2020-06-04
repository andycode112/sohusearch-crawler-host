#coding:utf-8
from flask import Blueprint,request
import os,json,datetime,pickle,re
#,configparser
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from bs4 import BeautifulSoup
from time import sleep
from model.sohunews_model import sohunews_model
from server.Logger import Logger

log = Logger(name='sohuapi')
sohuapi = Blueprint('sohuapi', __name__)

@sohuapi.route('/search',methods=['get'])
def serverdate():
    _keyword = request.values.get('keyword')
    ret = {}
    if _keyword != None and len(_keyword) > 0:
        # config = configparser.ConfigParser()
        # conf_file = open(os.path.join(os.getcwd(), "app.cfg"))
        # config.readfp(conf_file)
        # chromename = config.get("DEFAULT","a_chromename")
        # chrome_drive = os.path.join(os.getcwd(), chromename )
        option = ChromeOptions()
        option.add_experimental_option('excludeSwitches', ['enable-automation'])
        option.add_argument('headless') # set backgroud run option
        option.add_argument('--no-sandbox')
        option.add_argument('--disable-dev-shm-usage')
        browser = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver',options=option)
        browser.get('http://search.sohu.com/?keyword=%s' % _keyword)
        log.info('http://search.sohu.com/?keyword=%s' % _keyword)
        for i in range(1,4):
            sleep(3)
            browser.execute_script('window.scrollTo(0, document.body.scrollHeight)') # vertical sliding，scrollHeight
            print('lond '+str(i)+' page')
            log.info('lond '+str(i)+' page')
        res = browser.page_source
        if res != None and len(res) >0 :
            soup = BeautifulSoup(res, 'html.parser')
            mylist=[]
            # news = browser.find_element_by_id('news-list')
            for news in soup.select('.cards-small-img'):
                contenttitle = news.select('.cards-content-title')
                contentdesc = news.select('.cards-content-right-desc')
                contentcomm = news.select('.cards-content-right-comm')
                log.info(contenttitle + '     ' + contentdesc)
                newitem = sohunews_model()
                newitem.newtitle = contenttitle[0].text        
                newitem.newurl = contenttitle[0].next['href']
                newitem.newcontent = contentdesc[0].text        
                newitem.newcontenturl = contentdesc[0].select('a')[0]['href']        
                # 其他格式匹配. 如2016-12-24与2016/12/24的日期格式.
                # date_reg_exp = re.compile(r'\d{4}[-/]\d{1,2}[-/]\d{1,2}')
                # 根据正则查找所有日期并返回
                # matches_list=date_reg_exp.findall(contentcomm[0].text)
                #newtime = matches_list[0]
                newitem.newauthor_time = contentcomm[0].text # contentcomm[0].text.replace(newtime,'')
                newitem.newauthorurl = contentcomm[0].select('a')[0]['href']
                mylist.append(newitem)
                # print(newtitle.replace("\n", "") + '       ' + newauthor_time.replace("\n", ""))
            for news in soup.select('.cards-small-plain'):
                contenttitle = news.select('.plain-title')
                contentdesc = news.select('.plain-content-desc')
                contentcomm = news.select('.plain-content-comm')
                log.info(contenttitle + '     ' + contentdesc)
                newitem = sohunews_model()
                newitem.newtitle = contenttitle[0].text        
                newitem.newurl = contenttitle[0].next['href']
                newitem.newcontent = contentdesc[0].text        
                newitem.newcontenturl = contentdesc[0].select('a')[0]['href']        
                # 其他格式匹配. 如2016-12-24与2016/12/24的日期格式.
                # date_reg_exp = re.compile(r'\d{4}[-/]\d{1,2}[-/]\d{1,2}')
                # 根据正则查找所有日期并返回
                # matches_list=date_reg_exp.findall(contentcomm[0].text)
                #newtime = matches_list[0]
                newitem.newauthor_time = contentcomm[0].text # contentcomm[0].text.replace(newtime,'')
                newitem.newauthorurl = contentcomm[0].select('a')[0]['href']
                # print(newtitle.replace("\n", "") + '       ' + newauthor_time.replace("\n", ""))
                mylist.append(newitem)
            
            ret= {'success':True,'data':mylist,'msg':''} # pickle.dumps(mylist)#dict(mylist) 
        else:
            ret= {'success':False,'data':'','msg':'browser.get result is None or empty'}
        browser.quit()   
    else:
        ret= {'success':False,'data':'','msg':'the keyword is None or empty'}
    
    return ret #pickle.dumps(ret) json.dumps(ret,ensure_ascii=False)

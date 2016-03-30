# -*- coding: utf-8 -*-
import urllib2
from lxml import etree
import re
import os
for year in range(2011,2015): #年份
    for month in range(1,13): #月份
        for day in range(1,32): #日期
            if str(month)+str(day)=='229' or str(month)+str(day)=='230' or str(month)+str(day)=='231' or str(month)+str(day)=='431' or str(month)+str(day)=='631' or str(month)+str(day)=='931' or str(month)+str(day)=='1131':
                continue
            
            else:
                print(str(year)+'年'+ str(month) + '月' + str(day) + '日的数据...')
                for page_num in range(1, 20):
                    try:
                        response = urllib2.urlopen("http://www.abc.net.au/news/archive/"+str(year)+","+str("%02d" %month)+","+str("%02d" %day)+"?page="+str(page_num),timeout=60) 
                        urls_article = etree.HTML(response.read()).xpath('//ul[@class="article-index"]/li/h3/a/@href')
                    except:
                        print 'Failed to open this link'
                        continue
                
                    
                    for url_article in urls_article:
                        try:
                            sub_response = urllib2.urlopen("http://www.abc.net.au"+ url_article,timeout=60)
                            html=sub_response.read()
                            page=etree.HTML(html)
                            title = page.xpath('//div[@class="article section"]/h1')[0].text
                        except:
                            print 'Failed to open link:'+"http://www.abc.net.au"+ url_article
                            continue
                       
                        
                        if type(title)==str:
                            title=title
                        else:
                            title=''
                        link= sub_response.url
                        content = ''  #建立一个空白的string，在下面把contents这个list里面的string提取出来加到content里
                        contents = page.xpath('//div[@class="article section"]/p[not(@class="topics") and not(@class="published")]')
                        for i in contents:
                            if type(i.text)==str:
                                content=content+i.text
                            else:
                                continue
                        date= re.findall(r'\d\d\d\d-\d\d-\d\d', sub_response.url)
                        print date, title
                        #if not os.path.exists(r"H:\ABC\\results\\"+ str(year)+"-"+str("%02d" %month)+"-"+str("%02d" %day) + ".txt"):
                        f=open( str(year)+"-"+str("%02d" %month)+"-"+str("%02d" %day) + ".txt",'a')
                        f.writelines([title,'\n',date[0],'\n',link,'\n',content,'\n'])
                        f.close()
                   

                    
                        

            

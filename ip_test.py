import requests
from lxml import etree


for i in range(1,10):
        url = f'http://www.66ip.cn/{i}.html'
        print(url)
#目标

        header = {
                    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.42'
                    }
#伪装

        resp = requests.get(url,headers = header)
#发送请求

        resp.encoding = 'gbk'
#设置编码

#print(resp.text)
#接受响应

        e = etree.HTML(resp.text)
#创建可以提取数据的对象

        ips = e.xpath('//div[1]/table//tr/td[1]/text()')
#提取IP

        ports = e.xpath('//div[1]/table//tr/td[2]/text()')

#提取地址

        addrs = e.xpath('//div[1]/table//tr/td[3]/text()')

        for i,p,a in zip(ips,ports,addrs):

                    print(f"ip地址:{i}---port端口号:{p}---地址:{a}")

import requests
from lxml import etree

# 网站
url = "http://pic.netbian.com/index.html"

requese = requests.get(url)
cont = requese.content.decode("gbk")
html=etree.HTML(cont)

link = html.xpath('//ul[@class="clearfix"]/li/a/@href')
#获取属性的值的时候，需要给属性加上中括号[]
for i in link:
    url = "http://pic.netbian.com"+i
    requese = requests.get(url)
    cont = requese.content.decode("gbk")
    html=etree.HTML(cont)
    link=html.xpath('//div[@class="photo-pic"]/a/img/@src')
    imgname=html.xpath('.//@alt')[0]
    
    for i in link:
        link="http://pic.netbian.com"+i
        name='%s.jpg' % imgname
        requ=requests.get(link)
        img=requ.content
        
    with open('./imag/'+name, "wb") as f:
        f.write(img)
        print('现在正在下载的图片是%s' % name)

"""
requests/urllib
"""


# 导入模块
import requests
import urllib.request 
from urllib import request

# requests、urllib请求
url = 'https://www.baidu.com'
r = requests.get(url)
u = urllib.request.urlopen(url)
print(r)
print(u.read()) # read()方法返还网页内容

#输出结果
#<Response [200]>
#b'<html>\r\n<head>\r\n\t<script>\r\n\t\tlocation.replace(location.href.replace("https://","http://"));\r\n\t</script>\r\n</head>\r\n<body>\r\n\t<noscript><meta http-equiv="refresh" content="0;url=http://www.baidu.com/"></noscript>\r\n</body>\r\n</html>'


# 设置请求头，可以伪装成浏览器访问
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36'
}
response = requests.get(url, headers= headers)
print(response)

# urllib设置请求头
req = request.Request(url= url, headers= headers) # urllib设置请求头需要Request类来构建，再用request来请求,urlopen完成get请求爬取
urllib_req = request.urlopen(req)
print(urllib_req)

#输出结果
#<Response [200]>
#<http.client.HTTPResponse object at 0x037379F0>

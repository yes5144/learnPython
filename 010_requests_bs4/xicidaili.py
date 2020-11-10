import requests

from bs4 import BeautifulSoup

## http://c.biancheng.net/view/2011.html

## https://www.cnblogs.com/yizhenfeng168/p/6972946.html
## https://www.cnblogs.com/yizhenfeng168/p/6979339.html

# url = 'http://www.xicidaili.com'
url = 'http://ip.jiangxianli.com/?page=3'

headers = {
    'Accept':
    'image/webp,image/apng,image/*,*/*;q=0.8',
    'Accept-Encoding':
    'gzip, deflate',
    'Accept-Language':
    'zh-CN,zh;q=0.9,en;q=0.8',
    'Cache-Control':
    'no-cache',
    'Connection':
    'keep-alive',
    'Cookie':
    '',
    'Host':
    '',
    'Pragma':
    'no-cache',
    'Referer':
    'https://ip.jiangxianli.com/',
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36',
}

# response = requests.get(url, headers=headers)
html = '''
<table class="layui-table"><thead><tr><th>IP</th><th>端口</th><th>匿名度</th><th>类型</th><th width="160">位置</th><th>所属国</th><th>运营商</th><th>响应速度</th><th>存活时间</th><th>最后验证时间</th><th></th></tr></thead><tbody><tr><td>61.135.185.68</td><td>80</td><td>高匿</td><td>HTTP</td><td>中国 北京市 北京</td><td>中国</td><td>China Unicom Beijing</td><td>8毫秒</td><td>119天15小时</td><td>2020-08-22 18:00:40</td><td><button class="layui-btn layui-btn-sm btn-copy" data-url="http://61.135.185.68:80" data-unique-id="ecab9d38cfd8072ee45a3d5ffeab55ee">复制 </button><button class="layui-btn layui-btn-sm btn-speed " data-url="http://61.135.185.68:80" data-protocol="http" data-ip="61.135.185.68" data-port="80" data-unique-id="ecab9d38cfd8072ee45a3d5ffeab55ee">测速 </button></td></tr><tr><td>61.135.185.20</td><td>80</td><td>高匿</td><td>HTTP</td><td>中国 北京 北京市</td><td>中国</td><td>联通</td><td>10毫秒</td><td>118天19小时</td><td>2020-08-22 18:00:40</td><td><button class="layui-btn layui-btn-sm btn-copy" data-url="http://61.135.185.20:80" data-unique-id="c2d625db2391ff6d9f197087ed58f302">复制 </button><button class="layui-btn layui-btn-sm btn-speed " data-url="http://61.135.185.20:80" data-protocol="http" data-ip="61.135.185.20" data-port="80" data-unique-id="c2d625db2391ff6d9f197087ed58f302">测速 </button></td></tr><tr><td>61.135.185.38</td><td>80</td><td>高匿</td><td>HTTP</td><td>中国 北京 北京市</td><td>中国</td><td>联通</td><td>14毫秒</td><td>118天9小时</td><td>2020-08-22 18:00:40</td><td><button class="layui-btn layui-btn-sm btn-copy" data-url="http://61.135.185.38:80" data-unique-id="dc2f108bd4eeee394a6b7436a1f7260c">复制 </button><button class="layui-btn layui-btn-sm btn-speed " data-url="http://61.135.185.38:80" data-protocol="http" data-ip="61.135.185.38" data-port="80" data-unique-id="dc2f108bd4eeee394a6b7436a1f7260c">测速 </button></td></tr><tr><td>61.135.185.176</td><td>80</td><td>高匿</td><td>HTTP</td><td>中国 北京市 北京</td><td>中国</td><td>China Unicom Beijing</td><td>19毫秒</td><td>112天11小时</td><td>2020-08-22 18:00:40</td><td><button class="layui-btn layui-btn-sm btn-copy" data-url="http://61.135.185.176:80" data-unique-id="c3550ff705be333895c2bfdab7b4d477">复制 </button><button class="layui-btn layui-btn-sm btn-speed " data-url="http://61.135.185.176:80" data-protocol="http" data-ip="61.135.185.176" data-port="80" data-unique-id="c3550ff705be333895c2bfdab7b4d477">测速 </button></td></tr><tr><td>61.135.185.69</td><td>80</td><td>高匿</td><td>HTTP</td><td>中国 北京 北京</td><td>中国</td><td>联通</td><td>12毫秒</td><td>119天18小时</td><td>2020-08-22 18:00:40</td><td><button class="layui-btn layui-btn-sm btn-copy" data-url="http://61.135.185.69:80" data-unique-id="96ce3b66c2c2b4a328b8ac004d228841">复制 </button><button class="layui-btn layui-btn-sm btn-speed " data-url="http://61.135.185.69:80" data-protocol="http" data-ip="61.135.185.69" data-port="80" data-unique-id="96ce3b66c2c2b4a328b8ac004d228841">测速 </button></td></tr><tr><td>61.135.185.31</td><td>80</td><td>高匿</td><td>HTTP</td><td>中国 北京市 北京</td><td>中国</td><td>China Unicom Beijing</td><td>9毫秒</td><td>116天21小时</td><td>2020-08-22 18:00:40</td><td><button class="layui-btn layui-btn-sm btn-copy" data-url="http://61.135.185.31:80" data-unique-id="9f71fdbd4c5272b8fd4fc3e0f3f76d97">复制 </button><button class="layui-btn layui-btn-sm btn-speed " data-url="http://61.135.185.31:80" data-protocol="http" data-ip="61.135.185.31" data-port="80" data-unique-id="9f71fdbd4c5272b8fd4fc3e0f3f76d97">测速 </button></td></tr><tr><td>61.135.185.90</td><td>80</td><td>高匿</td><td>HTTP</td><td>中国 北京市 北京</td><td>中国</td><td>China Unicom Beijing</td><td>14毫秒</td><td>116天6小时</td><td>2020-08-22 18:00:40</td><td><button class="layui-btn layui-btn-sm btn-copy" data-url="http://61.135.185.90:80" data-unique-id="0d911c076d04d70f24747679d294093c">复制 </button><button class="layui-btn layui-btn-sm btn-speed " data-url="http://61.135.185.90:80" data-protocol="http" data-ip="61.135.185.90" data-port="80" data-unique-id="0d911c076d04d70f24747679d294093c">测速 </button></td></tr><tr><td>36.103.223.96</td><td>3128</td><td>透明</td><td>HTTP</td><td>中国 宁夏 中卫市</td><td>中国</td><td>电信</td><td>1.214秒</td><td>2天15小时</td><td>2020-08-22 18:00:40</td><td><button class="layui-btn layui-btn-sm btn-copy" data-url="http://36.103.223.96:3128" data-unique-id="d7f476e412d12d9a1ba5d7c55d287b54">复制 </button><button class="layui-btn layui-btn-sm btn-speed " data-url="http://36.103.223.96:3128" data-protocol="http" data-ip="36.103.223.96" data-port="3128" data-unique-id="d7f476e412d12d9a1ba5d7c55d287b54">测速 </button></td></tr><tr><td>61.135.185.153</td><td>80</td><td>高匿</td><td>HTTP</td><td>中国 北京市 北京</td><td>中国</td><td>China Unicom Beijing</td><td>18毫秒</td><td>113天6小时</td><td>2020-08-22 18:00:39</td><td><button class="layui-btn layui-btn-sm btn-copy" data-url="http://61.135.185.153:80" data-unique-id="a5170cb99e2e087f9632575f3b294792">复制 </button><button class="layui-btn layui-btn-sm btn-speed " data-url="http://61.135.185.153:80" data-protocol="http" data-ip="61.135.185.153" data-port="80" data-unique-id="a5170cb99e2e087f9632575f3b294792">测速 </button></td></tr><tr><td>61.135.185.152</td><td>80</td><td>高匿</td><td>HTTP</td><td>中国 北京 北京市</td><td>中国</td><td>联通</td><td>15毫秒</td><td>103天4小时</td><td>2020-08-22 18:00:39</td><td><button class="layui-btn layui-btn-sm btn-copy" data-url="http://61.135.185.152:80" data-unique-id="7d4cd8db9dd5a8b1925c602f81f3b200">复制 </button><button class="layui-btn layui-btn-sm btn-speed " data-url="http://61.135.185.152:80" data-protocol="http" data-ip="61.135.185.152" data-port="80" data-unique-id="7d4cd8db9dd5a8b1925c602f81f3b200">测速 </button></td></tr><tr><td>61.135.185.111</td><td>80</td><td>高匿</td><td>HTTP</td><td>中国 北京市 北京</td><td>中国</td><td>China Unicom Beijing</td><td>14毫秒</td><td>118天23小时</td><td>2020-08-22 18:00:39</td><td><button class="layui-btn layui-btn-sm btn-copy" data-url="http://61.135.185.111:80" data-unique-id="97216915c85d1ebc597d1071200506e5">复制 </button><button class="layui-btn layui-btn-sm btn-speed " data-url="http://61.135.185.111:80" data-protocol="http" data-ip="61.135.185.111" data-port="80" data-unique-id="97216915c85d1ebc597d1071200506e5">测速 </button></td></tr><tr><td>61.135.169.121</td><td>80</td><td>高匿</td><td>HTTP</td><td>中国 北京 北京市</td><td>中国</td><td>联通</td><td>9毫秒</td><td>116天13小时</td><td>2020-08-22 18:00:39</td><td><button class="layui-btn layui-btn-sm btn-copy" data-url="http://61.135.169.121:80" data-unique-id="bf65b68070c42792e9d8e3e5c3426580">复制 </button><button class="layui-btn layui-btn-sm btn-speed " data-url="http://61.135.169.121:80" data-protocol="http" data-ip="61.135.169.121" data-port="80" data-unique-id="bf65b68070c42792e9d8e3e5c3426580">测速 </button></td></tr><tr><td>188.226.141.61</td><td>8080</td><td>透明</td><td>HTTP</td><td>荷兰 North Holland 阿姆斯特丹</td><td>荷兰</td><td>DigitalOcean, LLC</td><td>3.164秒</td><td>5小时3分钟</td><td>2020-08-22 18:00:39</td><td><button class="layui-btn layui-btn-sm btn-copy" data-url="http://188.226.141.61:8080" data-unique-id="780aca103b5a65cadc50e12b78cfe619">复制 </button><button class="layui-btn layui-btn-sm btn-speed " data-url="http://188.226.141.61:8080" data-protocol="http" data-ip="188.226.141.61" data-port="8080" data-unique-id="780aca103b5a65cadc50e12b78cfe619">测速 </button></td></tr><tr><td>61.135.185.103</td><td>80</td><td>高匿</td><td>HTTP</td><td>中国 北京 北京市</td><td>中国</td><td>联通</td><td>116毫秒</td><td>118天9小时</td><td>2020-08-22 18:00:39</td><td><button class="layui-btn layui-btn-sm btn-copy" data-url="http://61.135.185.103:80" data-unique-id="2562b32d0946b37abf619b550ba25c20">复制 </button><button class="layui-btn layui-btn-sm btn-speed " data-url="http://61.135.185.103:80" data-protocol="http" data-ip="61.135.185.103" data-port="80" data-unique-id="2562b32d0946b37abf619b550ba25c20">测速 </button></td></tr><tr><td>61.135.185.12</td><td>80</td><td>高匿</td><td>HTTP</td><td>中国 北京 北京</td><td>中国</td><td>联通</td><td>11毫秒</td><td>119天18小时</td><td>2020-08-22 18:00:39</td><td><button class="layui-btn layui-btn-sm btn-copy" data-url="http://61.135.185.12:80" data-unique-id="e5533c6e94e5e39937a6be271833d678">复制 </button><button class="layui-btn layui-btn-sm btn-speed " data-url="http://61.135.185.12:80" data-protocol="http" data-ip="61.135.185.12" data-port="80" data-unique-id="e5533c6e94e5e39937a6be271833d678">测速 </button></td></tr></tbody></table>
'''
# soup = BeautifulSoup(response.text, 'lxml')
soup = BeautifulSoup(html, 'lxml')

tr_list = soup.find_all('tbody')

# print(tr_list)
for trs in tr_list:
    for tr in trs:
        print(tr.select('button')[0]['data-url'])
        # break

import requests
import datetime
import time
# 抢券的时间
start_time = "2018-11-28 19:59:50"
scheduled_time = "2018-11-28 20:00:10"
# 券的URL
couponUrl = "https://coupon.jd.com/ilink/couponSendFront/send_index.action?key=ec1c94aacffa466799846cb3645a4114&roleId=15853417&to=netease.jd.com"
# 券的Referer
referer = "https://sale.jd.com/act/Rbr24qKGXvyx8Wzn.html?cpdad=1DLSUE"
# 浏览器及版本
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'

# 将cookie转为字典
def get_cookie():
    with open("cookie.txt") as f:
        cookies = {}
        for line in f.read().split(';'):
            name, value = line.strip().split('=', 1)
            cookies[name] = value
        return cookies


# 配置Session的参数
session = requests.Session()
session.headers['User-Agent'] = user_agent
session.headers['Referer'] = referer
session.cookies = requests.utils.cookiejar_from_dict(get_cookie())


# 开始抢券
def getCoupon():
    while (datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') < start_time):
        print('尚未到开始时间',start_time,'，当前时间',datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), end='\r')
        time.sleep(1)

    print('尝试抢券中，至',scheduled_time,'结束。')
    cnt = 0
    now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    while (now < scheduled_time):
        # 当前时间

        r = session.get(couponUrl)
        cnt = cnt + 1
        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(now, end='\r')
        # print(r.text)
    else:
        print('结束，已尝试次数：',cnt)

def test():
    r = session.get(couponUrl)
    print(r.text)

if __name__ == '__main__':
    getCoupon()

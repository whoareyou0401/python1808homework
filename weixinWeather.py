
# pm2.5
import urllib.request
import time
from bs4 import BeautifulSoup
import itchat
def getPM25(cityname):
    c = time.localtime()
    times = time.strftime("%Y-%m-%d %X",c)
    site = "http://www.pm25.com/"+cityname+".html"
    page = urllib.request.urlopen(site)
    html = page.read()
root	ALL=(ALL:ALL) ALL
root	ALL=(ALL:ALL) ALL
    soup = BeautifulSoup(html.decode("utf-8"),"html.parser")
    city = soup.find(class_ = "bi_loaction_city")#城市名称
    aqi=soup.find("a",{"class","bi_aqiarea_num"})#AQI指数
    quality=soup.find(class_ = "bi_aqiarea_wuran wuranlevel_1")#空气质量等级
    result=soup.find("div",class_="bi_aqiarea_bottom")#空气质量描述
    weather = soup.find(class_ = "bi_info_weather")
    output=times+"\n"+city.text +"天气："+ weather.text +"\nAQI指数：" + aqi.text + "\n空气质量："+ quality.text  + result.text#
    print(output)
    print("*"*20+times+"*"*20)
    return output
itchat.auto_login(hotReload=True)
Help="""友情提示：
请输入城市拼音获取天气结果，如果无法识别，自动返回首都记录
"""
itchat.send(Help,toUserName="filehelper")
@itchat.msg_register(itchat.content.TEXT)
def getcity(msg):
    if msg["ToUserName"] != "filehelper":
            return
    print(msg["Text"])
    cityname = msg["Text"]
    result=getPM25(cityname)
    itchat.send(result,"filehelper")
if __name__=="__main__":
    itchat.run()

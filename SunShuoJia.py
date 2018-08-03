mport os
import requests
print(os.getcwd())
r = requests.get("https://www.baidu.com/")
print(r.url)
print(r.encoding)
print(r.text)
print("The end")
print("已完成")

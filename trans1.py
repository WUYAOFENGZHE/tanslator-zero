import requests
import json
import tkinter as tk

class zero(object):
    #初始化 URL，请求头，表单
    def __init__(self,word):
        self.url = "http://ifanyi.iciba.com/index.php?c=trans"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.142 Safari/537.36"
        }
        self.data = {
            "from":"auto",
            "to"  :"auto",
            "q"   : word
        }
    #发送post请求给指定URL返回响应的json字符串
    def first(self):
        response = requests.post(self.url,headers=self.headers,data=self.data)
        return response.content
    
    #将json字符串转为字典解析，并索引输出键OUT对应的值
    def second(self,data):

        dic = json.loads(data)
        q = dic["out"]
        return q

    #将第一个函数的值存入对象，并调用第二个函数
    def third(self):
        o = self.first()
        r = self.second(o)
        #控制删除文本框内之前的内容，插入爬虫结果
        massager.delete(0.0,'end')
        massager.insert('insert',r) 
        
#控制参数输入至文本框，调用zero(),及result.third
def f():
    word = massager.get(0.0,'end')
    result = zero(word)
    result.third()

#清除控制函数
def de():
    massager.delete(0.0, 'end')
#生成文本UI
root = tk.Tk()
root.title('翻译零号机')
root.geometry('400x200')
tip = tk.Label(root,text='请输入内容:')
tip.grid()
#文本区
massager = tk.Text(root,width=56,height=5)
massager.grid()
#按钮区
botton1 = tk.Button(root,text='翻译',width=8,command=f)
botton1.grid()
botton2 = tk.Button(root,text='清除',width=8,command=de)
botton2.grid()

root.mainloop()
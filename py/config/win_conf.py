#分辨率x,y
x=1920
y=1080
#底边栏
bottom=60
mx=1024
my=768+36
#winReg窗口起始范围
winReg1=(0,0,mx,y-my-bottom)#点亮窗口匹配范围
winReg11=(0,0,mx,my)#界面匹配范围
winReg2=(mx,0,mx,my)
winReg21=(x-mx,0,mx,my)
winReg3=(0,y-bottom-200,mx,my)
winReg31=(0,y-bottom-my,mx,my+bottom)
#3个窗口名称
winArr=['win1','win2','win3']
image_win1='./image/win/win1.png|./image/win/win11.png'
image_win2='./image/win/win2.png|./image/win/win21.png'
image_win3='./image/win/win3.png'

winConf={winArr[0]:[image_win1,winReg1,winReg11],winArr[1]:[image_win2,winReg2,winReg21],winArr[2]:[image_win3,winReg3,winReg31]}

#窗口开启状态
WinState={winArr[0]:True,winArr[1]:True,winArr[2]:True}

class window(object):
    def __init__(self,name):
        # 设置属性
        self.name = name
        self.image_win=winConf[name][0]
        self.winReg1=winConf[name][1]
        self.winReg=winConf[name][2]
        # 输出一个字符串(追踪对象属性信息变化)
    def __str__(self):  # __str__(self)不可以添加参数(形参)
        return "名字：%s 年龄：%s" % (self.name, self.winReg)

#宝图任务/运镖任务/挖宝任务(1:未接任务/2:正在执行/3:执行完成)
BtSignArr={winArr[0]:1,winArr[1]:1,winArr[2]:1}
YbSignArr={winArr[0]:1,winArr[1]:1,winArr[2]:1}
WbSignArr={winArr[0]:1,winArr[1]:1,winArr[2]:1}

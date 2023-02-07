from py.method.__init__ import *

#倒计时
def countdown(i):
    print('程序', i, '秒后开始执行！')
    while i > 0:
        print('倒数计时：', i )
        i = i - 1
        time.sleep(1) 
    print('')
    print('------------程序开始执行！-------------')

#把字符串按'|'切割
def word_cut(args):
    tup = []
    if '|' in args:
        re1 = args.split('|')
        return re1
    else:
        tup.append(args)
        return tuple(tup)
#循环找图，找到就返回图像中心点
def myLocateOnScreens(args,reg):
    arg = word_cut(args)
    for i in range(len(arg)):
        try:
            window=pyautogui.locateOnScreen(arg[i],confidence=0.95,region=reg)
        except:
            print('图片不存在:',arg[i])
            window=None
        if window is not None:
            return pyautogui.center(window)
        # else:
        #     print('imageUtil is not found!')
    return None

#循环找图，找到就返回图像中心点
def locateOnScreensForConf(args,confide,reg):
    arg = word_cut(args)
    for i in range(len(arg)):
        try:
            window=pyautogui.locateOnScreen(arg[i],confidence=confide,region=reg)
        except:
            print('图片匹配错误:',arg[i])
            window=None
        if window is not None:
            return pyautogui.center(window)
        # else:
        #     print('imageUtil is not found!')
    return None
#点亮窗口
def lightWin(name):
	image_win=winConf[name][0]
	winReg=winConf[name][1]
	point =locateOnScreensForConf(image_win,0.8,winReg)
	if point is not None:
		if name=='win1':
			point=[point[0]+200,point[1]]
		elif name=='win2':
			point=[point[0]-200,point[1]]
		leftMouse(point)
		time.sleep(0.5)
		return True
	else:
		logger.error('窗口:%s暂无匹配!',image_win)
		return False

#鼠标移动点位右键
def rightMouse(point):
    pyautogui.moveTo(point,duration=0.5)
    pyautogui.click(button='right')
    time.sleep(0.5)
#鼠标移动点位左键
def leftMouse(point):
    pyautogui.moveTo(point,duration=0.5)
    time.sleep(0.5)
    pyautogui.click(button='left')
#鼠标左键双击
def leftMouse2(point):
    pyautogui.moveTo(point,duration=0.5)
    pyautogui.click(button='left',clicks=2, interval=0.5)
    time.sleep(0.5)

#ESC清空界面窗口
def escBtn():
    time.sleep(0.5)
    pyautogui.press('esc')
    time.sleep(0.5)

#CTRL+A 挂机自动
def ctrlA():
    time.sleep(0.5)
    pyautogui.keyDown('ctrl')
    pyautogui.keyDown('a')
    pyautogui.keyUp('ctrl')
    pyautogui.keyUp('a')
    time.sleep(0.5)

#点击日常图标,根据图标获取任务NPC
def clickRC(name,rwImage):
    print('------------------',name,'点击日常图标','------------------')
    winReg=winConf[name][2]
    escBtn()
    ctrlA()
    point = myLocateOnScreens(image_rc,winReg)
    if point is not None:
        leftMouse(point)
        time.sleep(1)
        point = myLocateOnScreens(rwImage,winReg)
        if point is not None:
            leftMouse(point)
            return True
        else:
            print('------------------',name,'任务图标:',rwImage,'识别报错','------------------')
            return False
    else:
        print('------------------',name,'日常图标识别报错','------------------')
        return False


#鼠标悬浮任务栏
def mouseHoverToTask(name):
    if lightWin(name):
        winReg=winConf[name][2]
        point = myLocateOnScreens(image_rwl,winReg)
        if point is not None:
            pyautogui.moveTo(point[0],point[1]+30,duration=1)
            time.sleep(0.5)
            return True
        else:
            logger.error('注:%s任务栏未检测到,请检查!',name)
            return False

#判断任务栏任务状态
def isTask(rwImage,winReg):
    point =myLocateOnScreens(rwImage,winReg)
    if point is not None:
		#任务开启中...点击自动寻路
        leftMouse2(point)
        return True
    return False

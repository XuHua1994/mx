# -*- coding: utf-8 -*
from __init__ import *

def mainMethod():
	#循环时间
	t = 30
	#循环标志
	sign=True
	index=1
	while sign:
		for item in winArr:
			if lightWin(item):
				wbMethod(item)
				time.sleep(1)
		logger.info('第%d次挖宝！',index)
		index=index+1
		if index >30 or (WbSignArr[winArr[0]]==3 and WbSignArr[winArr[1]]==3 and WbSignArr[winArr[2]]==3):
			sign=False
		else:
			time.sleep(t)
	logger.info('--------挖宝结束--------')

if __name__ == "__main__":
	#设置当前文件路径
	os.chdir(sys.path[0])
	i = 3
	logger.info('程序', i, '秒后开始执行！')
	while i > 0:
		logger.info('倒数计时：%d', i )
		i = i - 1
		time.sleep(1)
	logger.info('程序开始执行！')
	#鼠标选中后停一下大于0.5秒 小于1.5秒
	time.sleep(0.5 + (1 * random.random()))
	mainMethod()
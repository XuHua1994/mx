#!/usr/bin/python
# -*- coding: utf-8 -*

from __init__ import *

sign=True
index=1
name='win1'

def cmMethod(name,indexWait):
	if indexWait>30:
		logger.error('wait timeout')
		return False
	winReg=winConf[name][2]
	#判断窗口开启状态
	if lightWin(name):
    	#判断是否处于接任务状态
		point=myLocateOnScreens(image_lqcmrw,winReg)
		if point is not None:
			leftMouse(point)
			time.sleep(0.5)
			rightMouse(point)
			if mouseHoverToTask(name):
				point=myLocateOnScreens(image_cmrw,winReg)
				if  point is not None:
					leftMouse2(point)
					return True
			logger.error('------win ERR------')
			return False
		else:
			logger.info('------Not completed 10 s later------')
			time.sleep(10)
			indexWait=indexWait+1
			return cmMethod(name,indexWait)
	else:
		return False



if __name__ == "__main__":
	while sign:
		logger.info('wait rw for num:%d',index)
		sign=cmMethod(name,0)
		if not sign:
			logger.error('除魔异常任务结束!')
			break
		if index<30:
			if index%6==0:
				for item in winArr:
					if lightWin(item):
						ctrlA()
			index=index+1
			if sign:
				time.sleep(60)
		else:
			logger.info('cm次数完成')
			sign=False
	logger.info('----------------cm end-------------------')
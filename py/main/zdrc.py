# -*- coding: utf-8 -*
from __init__ import *
#循环时间
t = 2*60
#主程序循环标志
sign=True
#循环次数
index=1
#挖宝次数(进入挖宝后index重新计数)
wbSign=0

if __name__ == "__main__":
	#设置当前文件路径
	os.chdir(sys.path[0])
	#倒计时
	countdown(5)
	while sign:
		logger.info('第 %d 次自动！', index)
		for item in winArr:
			if WinState[item]:
				if lightWin(item):
					logger.info('------------%s Light up ------------',item)
					#开启状态-执行逻辑
					# 1.判断任务情况:当前任务栏有无正在运行
					verdictSign=False
					if index==1:
						verdictSign=verdictTask(item)
					#2.执行流程方法
					if not verdictSign:
						zdMethod(item)
					logger.info(item,'- Task status:',BtSignArr[item],YbSignArr[item],WbSignArr[item])
					if BtSignArr[item]==3 and YbSignArr[item]==3 and WbSignArr[item]==3:
						WinState[item]=False
						logger.info(item,'- Task complete!')
				else:
					WbSignArr[item]=3
					logger.error('注:---------%s 窗口未打开或无法识别!',item)
		if WbSignArr[winArr[0]] > 1 and WbSignArr[winArr[1]] > 1 and WbSignArr[winArr[2]] > 1 :
			if WbSignArr[winArr[0]] == 3 and WbSignArr[winArr[1]] == 3 and WbSignArr[winArr[2]] == 3:
				sign=False
				logger.error('-------------窗口全部异常,请检查窗口!-------------')
			else:
				#都处于挖宝/终止状态加速循环时间
				logger.info('-------------处于挖宝/终止状态加速循环时间!-------------')
				t=20
		index=index+1
		if index >60 or (WbSignArr[winArr[0]] == 3 and WbSignArr[winArr[1]] == 3 and WbSignArr[winArr[2]] == 3):
			sign=False
		if sign:
			time.sleep(t)
			countdown(5)
		
	logger.info('-------------自动任务结束-------------')
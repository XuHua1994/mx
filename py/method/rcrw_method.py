
from py.method.share_method import *

#准备工作:点击物品->整理->行囊->吃草
def preparatoryWork(name):
    winReg=winConf[name][2]
    point = myLocateOnScreens(image_wp,winReg)
    if point is not None:
        leftMouse(point)
        #避错:整理
        point = myLocateOnScreens(image_zl,winReg)
        if point is not None:
            leftMouse(point)
        else:
            print('注:',name,'点击整理失败,请检查程序!')
        #避错:先点击行囊
        point = myLocateOnScreens(image_xn,winReg)
        if point is not None:
            leftMouse(point)
        else:
            print('注:',name,'点击行囊失败,请检查程序!')
        time.sleep(0.5)
        #避错:吃草
        point = myLocateOnScreens(image_cao,winReg)
        if point is not None:
            rightMouse(point)
        else:
            print('注:',name,'物品-行囊中没有避邪草,将影响挖宝进程!')
        time.sleep(0.5)
        return True
    else:
        print('注:',name,'点击物品失败,请检查程序!')
        return False

#打宝图任务
def btMethod(name):
	winReg=winConf[name][2]
	global BtSignArr
	if BtSignArr[name]==1:
		#点击日常任务图标
		if clickRC(name,image_btrw):
			time.sleep(10)
			point = myLocateOnScreens(image_dtzybt,winReg)
			if point is not None:
				leftMouse(point)
				point = myLocateOnScreens(image_jxlq,winReg)
				if point is not None:
					leftMouse(point)
				BtSignArr[name]=2
				time.sleep(1)
				#判断宝图任务是否完成
				point = myLocateOnScreens(image_btwc,winReg)
				if point is not None:
					BtSignArr[name]=3
					#挖宝完成执行运镖任务
					ybMethod(name)
					return
			else:
				point = myLocateOnScreens(image_btrwIns,winReg)
				if point is not None:
					leftMouse(point)
					BtSignArr[name]=2
					return
				else:
					BtSignArr[name]==3
					print('注:',name,'宝图任务匹配失败,执行运镖任务!')
					ybMethod(name)
					return
		else:
			BtSignArr[name]=3
			print('注:',name,'宝图任务图标匹配失败,执行运镖任务!')
			ybMethod(name)
	elif (BtSignArr[name]==2):
		#场景:宝图任务执行中,先判断是否完成
		point = myLocateOnScreens(image_btwc,winReg)
		if point is not None:
			BtSignArr[name]=3
			#挖宝完成执行运镖任务
			rightMouse(point)
			ybMethod(name)
		else:
			#流程:宝图任务-10个-继续领取
			point = myLocateOnScreens(image_jxjq,winReg)
			if point is not None:
				print('------------',name,'继续接取宝图','------------')
				leftMouse(point)
			else:
				print('------------',name,'BT_ING','------------')

#运镖任务
def ybMethod(name):
	winReg=winConf[name][2]
	global YbSignArr
	if YbSignArr[name]==1:
		#点击日常任务图标
		if clickRC(name,image_ybrw):
			time.sleep(10)
			#点击,领取任务
			point = myLocateOnScreens(image_hsby,winReg)
			if point is not None:
				leftMouse(point)
				time.sleep(2)
				point = myLocateOnScreens(image_jxlq,winReg)
				if point is not None:
					leftMouse(point)
				#判断是否运完镖局
				point = myLocateOnScreens(image_ybwc,winReg)
				print('运镖完成判断:',point)
				if point is not None:
					YbSignArr[name]=3
					escBtn()
					ctrlA()
					print(name,'- 运镖任务完成->挖宝任务')
					wbMethod(name)
				else:
					YbSignArr[name]=2
					return
			else:
				YbSignArr[name]=3
				print('注:',name,'运镖任务默认完成,执行挖宝任务!')
				# YB_To_WB(name,winReg)
				escBtn()
				ctrlA()
				wbMethod(name)
		else:
			YbSignArr[name]=3
			print('注:',name,'运镖任务图标匹配失败,执行挖宝')
			escBtn()
			ctrlA()
			wbMethod(name)
	elif (YbSignArr[name]==2):
		#场景:运镖任务执行中,先判断是否完成
		point = myLocateOnScreens(image_ybwc,winReg)
		if point is not None:
			YbSignArr[name]=3
			#运镖任务完成->挖宝
			escBtn()
			ctrlA()
			print(name,'- 运镖任务完成->挖宝任务')
			wbMethod(name)
		else:
			print('------------',name,'YB_ING','------------')

#挖宝任务				
def wbMethod(name):
	winReg=winConf[name][2]
	global WbSignArr
	if WbSignArr[name]==1:
		print(name,'- 挖宝任务开始')
		#物品
		if preparatoryWork(name):
			#右键宝图开始挖宝
			point = myLocateOnScreens(image_bt,winReg)
			if point is not None:
				rightMouse(point)
				WbSignArr[name]=2
				escBtn()
				ctrlA()
				if not mouseHoverToTask(name):
					return
				if isTask(image_wbrwIns,winReg):
					print('---------------',name,' -wbrw -ING ---------------')
				else:
					print('---------------',name,' -wbrw -ERR1 ---------------')
					WbSignArr[name]=3
					print('注:',name,'点击宝图失败,请检查程序!由于未检索到宝图即当完成处理!')
			else:
				if not mouseHoverToTask(name):
					return
				if isTask(image_wbrwIns,winReg):
					print('---------------',name,' -wbrw -ING ---------------')
				else:
					print('---------------',name,' -wbrw -ERR2 ---------------')
					WbSignArr[name]=3
					print('注:',name,'点击宝图失败,请检查程序!由于未检索到宝图即当完成处理!')
		else:
			WbSignArr[name]=3
	elif WbSignArr[name]==2:
		print('---------------',name,' -wbrw -ING ---------------')
		point=myLocateOnScreens(image_tc,winReg)
		if point is not None:
			print('------判断弹窗存在-取消------')
			leftMouse2(point)
		#启动
		point=myLocateOnScreens(image_jxsy,winReg)
		if point is not None:
			leftMouse(point)
			if not mouseHoverToTask(name):
				return
			if isTask(image_wbrwIns,winReg):
				print('---------------',name,' -wbrw -ING ---------------')
			else:
				print('---------------',name,' -wbrw -ERR3 ---------------')
				WbSignArr[name]=3
				print('注:',name,'点击宝图失败,请检查程序!由于未检索到宝图即当完成处理!')
		else:
			if not mouseHoverToTask(name):
				return
			if isTask(image_wbrwIns,winReg):
				print('---------------',name,' -wbrw -ING ---------------')
			else:
				print('---------------',name,' -wbrw -ERR4 ---------------')
				WbSignArr[name]=3
				print('注:',name,'点击宝图失败,请检查程序!由于未检索到宝图即当完成处理!')
		
# 判断任务情况:当前任务栏有无正在运行
def verdictTask(name):
	winReg=winConf[name][2]
	print('---------------',name,' normal start ---------------')
	#判断自动流程进程
	global BtSignArr,YbSignArr,WbSignArr
	preparatoryWork(name)
	escBtn()
	ctrlA()
	if not mouseHoverToTask(name):
		return False

	#判断宝图任务是否开启状态
	if isTask(image_btrwIns,winReg):
		print('------------',name,'-btrw -ING','------------')
		BtSignArr[name]=2
		return True
		
	#判断运镖任务是否开启
	if isTask(image_ybrwIns,winReg):
		print('------------',name,'-ybrw -ING','------------')
		BtSignArr[name]=3
		YbSignArr[name]=2
		return True
	#判断挖宝任务是否开启
	if isTask(image_wbrwIns,winReg):
		print('------------',name,'-wbrw -ING','------------')
		BtSignArr[name]=3
		YbSignArr[name]=3
		WbSignArr[name]=2
		return True
	#场景未匹配进行基础流程
	return False

#日常任务流程
def zdMethod(name):
	winReg=winConf[name][2]
	global BtSignArr,YbSignArr,WbSignArr
	ctrlA()
	#宝图任务未完成
	if BtSignArr[name]<3:
		btMethod(name)
		return
	#宝图任务完成->运镖任务未完成
	if YbSignArr[name]<3 and BtSignArr[name]==3:
		ybMethod(name)
		return
	#运镖任务完成->挖宝任务
	if WbSignArr[name]<3 and YbSignArr[name]==3:
		wbMethod(name)
		return
	
	#场景:宝图任务完成->接镖局任务
	#流程:点击日常->点击运镖图标->点击运镖任务
	point1 = myLocateOnScreens(image_btwc,winReg)
	if point1 is not None:
		BtSignArr[name]==3
		ybMethod(name)
		return
	#场景:运镖任务完成->挖宝任务
	#流程:打开物品栏->整理->查询宝图
	point2 = myLocateOnScreens(image_ybwc,winReg)
	if point2 is not None:
		YbSignArr[name]=3
		wbMethod(name)
		return
#!/usr/bin/python
# -*- coding: utf-8 -*
from __init__ import *
import threading
sign=True
#线程开关
threadSign=False
#1.判断副本类型
def fbMethod(titel,fb_config,winReg):
    global sign,threadSign
    #检测的titel,左键双击寻路
    leftMouse2(titel)
    #5秒判断一次
    time.sleep(5)
    image_zd=fb_config[1]
    image_bossRw=fb_config[2]
    image_wait=fb_config[3]
    image_boss=fb_config[4]
    #npc战斗弹窗(普通/Boss)
    image_zd=myLocateOnScreens(image_zd,winReg)
    bossRw=myLocateOnScreens(image_bossRw,winReg)
    if image_zd is not None:
        leftMouse(image_zd)
        time.sleep(210)
        sign=True
    elif  bossRw is not None:
        logger.info('------BOSS执行逻辑------')
        wait=myLocateOnScreens(image_wait,winReg)
        if wait is not None:
            leftMouse(wait)
            time.sleep(0.5)

        #点亮窗口,取消自动
        for item in winArr:
            if item!=team and lightWin(item):
                leftMouse(point)
                escBtn()
                    
        lightWin(team)
        escBtn()
        leftMouse(titel)
        leftMouse(bossRw)
        # BOSS存在即右键集火,否则Ctrl+A
        boss=myLocateOnScreens(image_boss,winReg)
        if boss is not None:
            logger.info('boss is not None')
            boss=[boss[0],boss[1]-30]
        else:
            logger.info('boss is None')
        while boss is not None:
            logger.info('--------BOSS EXIST 集火主怪----------')
            for item in winArr:
                imagePath=winConf[item][0]
                winReg=winConf[item][1]
                #判断窗口开启状态
                point =myLocateOnScreensForWins(imagePath,0.8,winReg)
                if lightWin(item):
                    winReg=winConf[item][2]
                    time.sleep(0.5)
                    boss=myLocateOnScreens(image_boss,winReg)
                    rightMouse(boss)
                    time.sleep(0.5)
                    rightMouse(boss)
            logger.info('存在窗口集火主怪')
            time.sleep(10)
        return False
    else:
        logger.info('------未匹配任务,请稍候------')
        if index>30:
            logger.error('程序异常-终止!')
            sign =  False
        sign = True

def isBoss():
    

if __name__ == "__main__":
    team='win1'
    #判断窗口开启状态
    lightWin(team)
    winReg=winConf[team][2]
    #副本任务逻辑
    #首先锁定任务栏,判断副本类型
    fb_name=None
    index=1
    while fb_name is None:
        if mouseHoverToTask(team):
            for item in fbArr:
                image_title=fbConf[item][0]
                point=myLocateOnScreens(image_title,winReg)
                if point is not None:
                    fb_name=item
                    logger.info('当前副本为:%s',item)
                    #开启判断boss线程
                    T1 = threading.Thread(target=isBoss, name="T1")
                    T1.start()
                    index=1
                    while sign:
                        #首先判断有没有死士弹窗
                        # ssjl=myLocateOnScreens(image_ssjl,winReg)
                        # if ssjl is not None:
                        #     logger.info('------检测到死士奖励弹窗,等候20s,右键取消------')
                        #     time.sleep(30)
                        #     rightMouse(ssjl)
                        # fbConf[fb_name]
                        
                        # 窗口循环挂机自动
                        for item in winArr:
                            if lightWin(item):
                                ctrlA()
                        if index>15:
                            break
                        time.sleep(5*60)
                        index+=1
                else:
                    logger.error('当前副本无法识别,循环计数:%d',index)
                    if index>20:
                        break
                    index=index+1
                    time.sleep(10)
        else:
            if index>20:
                break
            index=index+1
            time.sleep(5)
            


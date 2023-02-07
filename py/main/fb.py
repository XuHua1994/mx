#!/usr/bin/python
# -*- coding: utf-8 -*
from __init__ import *


#1.判断副本类型
def fbMethod(titel,fb_config,winReg):
    leftMouse(titel)
    image_zd=fb_config[1]
    image_bossRw=fb_config[2]
    image_wait=fb_config[3]
    image_boss=fb_config[4]
    time.sleep(5)
    point=myLocateOnScreens(image_zd,winReg)
    bossRw=myLocateOnScreens(image_bossRw,winReg)
    if point is not None:
        leftMouse(point)
        time.sleep(150)
        return True
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
        boss=locateOnScreensForConf(image_boss,0.8,winReg)
        if boss is not None:
            logger.info('boss is not None')
            while boss is not None:
                logger.info('--------BOSS EXIST 集火主怪----------')
                for item in winArr:
                    #判断窗口开启状态
                    if lightWin(item):
                        winReg=winConf[item][2]
                        time.sleep(0.5)
                        boss=locateOnScreensForConf(image_boss,0.8,winReg)
                        if boss is not None:
                            boss=[boss[0],boss[1]-60]
                            rightMouse(boss)
                            time.sleep(0.5)
                            rightMouse(boss)
                            logger.info('存在窗口集火BOSS')
                        else:
                            ctrlA()
                            logger.info('未检测到BOSS,自动')
                time.sleep(10)
            for item in winArr:
                #判断窗口开启状态
                if lightWin(item):
                    ctrlA()
        else:
            logger.info('boss is None')
        return False
    else:
        logger.info('------未匹配任务,请稍候------')
        if index>30:
            logger.error('程序异常-终止!')
            return False
        return True

sign=True
index=1

if __name__ == "__main__":
    team='win1'
    #判断窗口开启状态
    lightWin(team)
    winReg=winConf[team][2]
    #副本任务逻辑
    #首先锁定任务栏,判断副本类型
    fb_name=None
    image_title=None
    image_zd=None
    image_bossRw=None
    while fb_name is None:
        if mouseHoverToTask(team):
            for item in fbArr:
                image_title=fbConf[item][0]
                point=myLocateOnScreens(image_title,winReg)
                if point is not None:
                    fb_name=item
                    logger.info('当前副本为:%s',item)
                    break
        if fb_name is None:
            logger.error('当前副本无法识别,请检测任务栏!')
            time.sleep(30)

    while sign:
        #首先判断有没有死士弹窗
        ssjl=myLocateOnScreens(image_ssjl,winReg)
        if ssjl is not None:
            logger.info('------检测到死士奖励弹窗,等候20s,右键取消------')
            time.sleep(30)
            rightMouse(ssjl)
        if mouseHoverToTask(team):
            titel=myLocateOnScreens(image_title,winReg)
            if titel is not None:
                sign=fbMethod(titel,fbConf[fb_name],winReg)
                index=index+1      
            else:
                logger.error('------当前副本无法识别!------')
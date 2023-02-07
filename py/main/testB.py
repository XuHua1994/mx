#!/usr/bin/python
# -*- coding: utf-8 -*
from __init__ import *
fb_config=fbConf['邪神']
image_zd=fb_config[1]
image_bossRw=fb_config[2]
image_wait=fb_config[3]
image_boss=fb_config[4]
boss=locateOnScreensForConf(image_boss,0.8,winReg11)
if boss is not None:
    logger.info('boss is not None')
    while boss is not None:
        logger.info('--------BOSS EXIST 集火主怪----------')
        for item in winArr:
            imagePath=winConf[item][0]
            winReg=winConf[item][1]
            #判断窗口开启状态
            point =locateOnScreensForConf(imagePath,0.8,winReg)
            if lightWin(item):
                winReg=winConf[item][2]
                time.sleep(0.5)
                boss=locateOnScreensForConf(image_boss,0.8,winReg)
                boss=[boss[0],boss[1]-60]
                rightMouse(boss)
                time.sleep(0.5)
                rightMouse(boss)
else:
    logger.info('boss is None')

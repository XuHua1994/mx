#!/usr/bin/python
# -*- coding: utf-8 -*
from __init__ import *

sign=True
index=1
if __name__ == "__main__":
	while sign:
		logger.info('zdgj for num:%d',index)
		if index<30:
			for item in winArr:
				if lightWin(item):
					ctrlA()
			index=index+1
			time.sleep(180)
		else:
			sign=False
	logger.info('----------------gj end-------------------')
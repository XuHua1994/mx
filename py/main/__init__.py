import pyautogui, time, os,sys, random, logging
# 常用方式2
sys.path.insert(0, '.')  # 直接添加
from py.config.log_conf import *
from py.config.constant import *
from py.config.win_conf import *
from py.config.fb_conf import *
from py.method.rcrw_method import *
from py.method.share_method import *

logger = get_logger(os.path.basename(sys.argv[0]).split('.')[0]+'.log')

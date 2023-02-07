import pyautogui, time, os,sys, logging
sys.path.insert(0, '.')  # 直接添加
from py.config.log_conf import *
from py.config.constant import *
from py.config.win_conf import *
logger = get_logger(os.path.basename(sys.argv[0]).split('.')[0]+'.log')
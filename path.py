# encoding: UTF-8

"""
用于backtesting的运行目录环境设置
"""

import os
import sys

# 将根目录路径添加到环境变量中
ROOT_PATH =os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
sys.path.append(ROOT_PATH)
# 将功能模块的目录路径添加到环境变量中
# 若各目录下存在同名文件可能导致异常，请注意测试
MODULE_PATH = {}
MODULE_PATH['EventEngine'] = os.path.join(ROOT_PATH, 'EventEngine')
MODULE_PATH['Stock'] = os.path.join(ROOT_PATH, 'Stock')
# 添加到环境变量中
for path in MODULE_PATH.values():
    if path not in sys.path:
        sys.path.append(path)
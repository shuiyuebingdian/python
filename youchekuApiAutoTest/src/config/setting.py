# _*_ coding:utf-8 _*_
import os
import sys

# 根据当前文件的位置获取项目的绝对路径，因此本文件不能移动
from configparser import ConfigParser

from src.common.constant import ENCODING

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
# 把项目路径添加到系统变量中
sys.path.append(BASE_DIR)

# 配置文件
TEST_CONFIG = os.path.join(BASE_DIR, "config", "conf.ini")
# 测试用例模板文件
SOURCE_FILE = os.path.join(BASE_DIR, "test_api")
# excel测试用例结果文件
TARGET_FILE = os.path.join(BASE_DIR, "report", "excelReport")
# 测试用例报告
TEST_REPORT = os.path.join(BASE_DIR, "report")
# 测试用例程序文件
TEST_CASE = os.path.join(BASE_DIR, "src", "test_api")
# 日志文件路径
LOG_PATH = os.path.join(BASE_DIR, "log")

CONFIG = ConfigParser()
CONFIG.read(TEST_CONFIG, encoding=ENCODING)

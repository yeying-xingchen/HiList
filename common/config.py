import toml
import logging as log

'''
单项目日志系列配置
'''

# loggin基础配置
log.basicConfig(
    filename= "./run.log",  # 日志记录文件位置
    format= '[%(asctime)s] %(name)s - %(levelname)s - %(module)s : %(message)s', # 时间-项目名称-信息等级-信息所属模块-信息
    datefmt= '%Y-%m-%d %H:%M:%S', # 时间记录的格式
    level=0,
)


import os
path = os.getcwd() + "\\config.toml"

def get_port():
    """获取端口，若不存在则返回80"""
    try:
        config = toml.load(path)
        return config['website']['port']
    except KeyError:
        return 80

def get_host():
    """获取主机地址，若不存在则返回'0.0.0.0'"""
    try:
        config = toml.load(path)
        return config['website']['host']
    except KeyError:
        return "0.0.0.0"

def get_website_name():
    """获取网站名称，若不存在则返回'HiList'"""
    try:
        config = toml.load(path)
        if config['website']['url'] == "HiList":
            log.warning(f"网站名称未设置！默认为 HiList，请前往配置文件修改。")
        return config['website']['url']
    except KeyError:
        return "HiList"
    
def get_db_info() -> dict:
    """获取数据库信息"""
    try:
        config = toml.load(path)
        return config['database']
    except KeyError:
        log.error(f"数据库信息未设置！请前往配置文件修改。")
        return 0
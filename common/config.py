import toml
import logging as log
import os

CONFIG_PATH = os.path.join(os.getcwd(), "config.toml")

_config = None

def _load_config():
    """加载配置文件并缓存结果"""
    global _config
    if _config is None:
        try:
            _config = toml.load(CONFIG_PATH)
        except (FileNotFoundError, toml.TomlDecodeError):
            log.error("配置文件加载失败: %s", CONFIG_PATH)
            _config = {}  # 返回空字典避免后续KeyError
    return _config

def _save_config():
    """保存配置到文件"""
    global _config
    try:
        # 保存到文件
        with open(CONFIG_PATH, 'w', encoding='utf-8') as f:
            toml.dump(_config, f)
        return _config
    except (IOError, toml.TomlEncodeError) as e:
        log.error("配置文件保存失败: %s", CONFIG_PATH)
        return _config

def get_port(default=80):
    """获取端口配置"""
    return _config.get('website', {}).get('port', default)

def get_host(default="0.0.0.0"):
    """获取主机配置"""
    return _config.get('website', {}).get('host', default)

def get_website_name(default="HiList"):
    """获取网站名称"""
    name = _config.get('website', {}).get('name', default)
    if name == "HiList":
        log.warning("网站名称未设置! 默认为 HiList，请修改配置文件")
    return name

def get_db_info() -> dict:
    """获取数据库配置"""
    config = _load_config()
    db_config = config.get('database', {})
    if not db_config:
        db_config = {
            "host": "127.0.0.1",
            "port": 3306,
            "database": "hilist",
            "user": "root",
            "password": "123456"
        }
        log.error("数据库配置缺失! 请检查配置文件")
    return db_config

# 日志初始化（应放在模块底部）
log.basicConfig(
    filename="./run.log",
    format='[%(asctime)s] %(name)s - %(levelname)s - %(module)s : %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    level=log.INFO  # 使用标准日志级别
)

# 加载配置
_load_config()

# 共用配置
import logging.config
from conf import settings


# 用户认证装饰器
def auth(func):
    from cose import src
    def inner(*args, **kwargs):
        if src.user_info['name']:
            res = func(*args, **kwargs)
            return res
        else:
            src.login()
    return inner


# 日志获取
def get_logger(name):
    logging.config.dictConfig(settings.LOGGING_DIC)
    logger = logging.getLogger(name)
    return logger

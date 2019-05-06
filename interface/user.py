# 用户接口层
from db import db_handles
from lib import common
logger = common.get_logger('用户操作')
# 用户注册接口
def register_interface(name,pwd,balance=15000):
    user_dic = db_handles.select(name)
    if user_dic:
        return False,'用户已存在'
    user_dic = {
        'name':name,'pwd':pwd,'balance':balance,
        'flow':[],'shopping_cart':{}
    }
    info = '用户[%s]注册成功'%name
    user_dic['flow'].append(info)
    db_handles.save(user_dic)
    logger.info(info)
    return True,'注册成功'

# 登录接口
def login_interface(name,pwd):
    user_dic = db_handles.select(name)
    if not user_dic:
        return False,'用户不存在!'
    if pwd == user_dic['pwd']:
        info = '用户[%s]登录成功'%name
        logger.info(info)
        return True,'登陆成功！'
    else:
        return False,'密码错误'

# 查询余额
def check_balance(name):
    user_dic = db_handles.select(name)
    return user_dic['balance']

# 注销用户
def logout_interface(name):
    from cose import src
    src.user_info['name'] = None
    return '用户[%s]已注销'%name

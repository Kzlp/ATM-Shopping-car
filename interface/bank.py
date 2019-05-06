# ATM业务接口
from db import db_handles
from lib import common
logger = common.get_logger('ATM')
# 提现接口
def withdraw_interface(name,money):
    user_dic = db_handles.select(name)
    money1 = money*1.05
    money2 = money*0.05
    if user_dic['balance'] >= money1:
        user_dic['balance'] -= money1
        info = '用户[%s]本次提现金额为[%s],手续费为[%s]'%(name,money,money2)
        user_dic['flow'].append(info)
        db_handles.save(user_dic)
        logger.info(info)
        return True,info
    else:
        return False,'额度不足！'

# 转账接口
def transfer_interface(from_name,to_name,money):
    to_name_dic = db_handles.select(to_name)
    if not to_name_dic:
        return False,'目标用户不存在!'
    from_name_dic = db_handles.select(from_name)
    if from_name_dic['balance'] >= money:
        from_name_dic['balance'] -=money
        to_name_dic['balance'] += money
        info = '用户[%s]给用户[%s]转账金额为[%s],当前可用额度为[%s]'\
               %(from_name,to_name,money,from_name_dic['balance'])
        info1='用户[%s]给你转账人民币[%s]'%(from_name,money)
        from_name_dic['flow'].append(info)
        to_name_dic['flow'].append(info1)
        db_handles.save(from_name_dic)
        db_handles.save(to_name_dic)
        logger.info(info)
        return True,info
    else:
        return '额度不足!'

# 还款接口
def repay_interface(name,money):
    user_dic = db_handles.select(name)
    user_dic['balance'] += money
    info='用户[%s]本次还款金额为[%s],当前可用额度为[%s]'%(name,money,user_dic['balance'])
    user_dic['flow'].append(info)
    db_handles.save(user_dic)
    logger.info(info)
    return '还款成功'
# 查看流水
def check_flow_interface(name):
    user_dic = db_handles.select(name)
    return user_dic['flow']

# 支付接口
def pay_interface(name,cost):
    user_dic = db_handles.select(name)
    if user_dic['balance'] >= cost:
        user_dic['balance'] -= cost
        user_dic['shopping_cart'] = {}
        info = '用户[%s]购物本次消费金额为[%s]'%(name,cost)
        user_dic['flow'].append(info)
        logger.info('用户[%s]购物本次消费金额为[%s]'%(name,cost))
        db_handles.save(user_dic)
        return '支付成功'
    else:
        return '额度不足!'

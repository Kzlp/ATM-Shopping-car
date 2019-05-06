# 购物接口
from db import db_handles
from lib import common
logger = common.get_logger('购物')
# 添加购物车
def add_shop_cart_interface(name,shopping_cart):
    user_dic = db_handles.select(name)
    user_dic['shopping_cart'] = shopping_cart
    info = '用户[%s]成功添加商品[%s]到购物车'%(name,shopping_cart)
    user_dic['flow'].append(info)
    logger.info(info)
    db_handles.save(user_dic)
    return True,'成功添加到购物车'

# 查看购物车
def check_shop_cart_interface(name):
    user_dic = db_handles.select(name)
    if user_dic['shopping_cart']:
        return True, user_dic['shopping_cart']
    else:
        return False,'购物车已清空!'
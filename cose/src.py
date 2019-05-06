user_info={
    'name':None
} # 记录用户登录信息
from interface import user,bank,shop
from lib import common
from db import db_handles

def register():
    while True:
        print('注册页面'.center(50,'='))
        name = input('请输入注册名:')
        pwd = input('请输入注册密码:')
        conf_pwd = input('请输入注册密码:')
        if pwd == conf_pwd:
            flag,msg = user.register_interface(name,pwd)
            if flag:
                print(msg)
                break
            else:
                print(msg)

def login():
    if user_info['name']:
        return False,'不需要重复登陆'
    while True:
        print('登录页面'.center(50, '='))
        name = input('请输入登录名>>:')
        pwd = input('请输入密码:')
        flag,msg = user.login_interface(name,pwd)
        if flag:
            user_info['name'] = name
            print(msg)
            break
        else:
            print(msg)
            break

@common.auth
def check_balance():
    print('查询余额'.center(50, '='))
    msg = user.check_balance(user_info['name'])
    print('当前余额为[%s]'%msg)
@common.auth
def withdraw():
    print('提现页面'.center(50, '='))
    while True:
        money = input('请输入提现金额:')
        if money.isdigit():
            money = int(money)
            flag,msg = bank.withdraw_interface(user_info['name'],money)
            if flag:
                print(msg)
                break
            else:
                print(msg)

@common.auth
def transfer():
    while True:
        print('转账页面'.center(50, '='))
        to_name = input('请输入目标账户名>>:')
        money = input('请输入转账金额>>:')
        if money.isdigit():
            money = int(money)
            flag,msg = bank.transfer_interface(user_info['name'],to_name,money)
            if flag:
                print(msg)
                break
            else:
                print(msg)
        else:
            print('输入有误！')

@common.auth
def repay():
    while True:
        print('还款页面'.center(50, '='))
        money = input('请输入还款金额>>:')
        if money.isdigit():
            money = int(money)
            msg = bank.repay_interface(user_info['name'],money)
            print(msg)
            break
        else:
            print('输入有误！')
@common.auth
def check_flow():
    user_flow = bank.check_flow_interface(user_info['name'])
    for line in user_flow:
        print(line)


@common.auth
def shopping():
    shopping_cart = {}
    print('购物页面'.center(50, '='))
    good_list = [
        ['iphone',1000],
        ['袜子',10],
        ['衣服',800],
        ['裤子',900]
    ]
    cost = 0
    user_money= user.check_balance(user_info['name'])
    while True:
        for k,v in enumerate(good_list):
            print(k,v)
        shop_num = input('请输入商品序号q/Q退出>>；')
        if shop_num.isdigit():
            shop_num = int(shop_num)
            if shop_num >= 0 and shop_num <len(good_list):
                good_name,good_price = good_list[shop_num]
                if user_money >= good_price:
                    if good_name in shopping_cart:
                        shopping_cart[good_name] +=1
                    else:
                        shopping_cart[good_name] = 1
                    cost += good_price
                    flag,msg = shop.add_shop_cart_interface(user_info['name'],shopping_cart)
                    if flag:
                        print(msg)
                        print(shopping_cart)
                else:
                    print('额度不足！')
        elif shop_num == 'q' or 'Q':
            if cost == 0:break
            confirm = input('确认支付y/n取消>>:')
            if confirm == 'y':
                msg = bank.pay_interface(user_info['name'],cost)
                print(msg)
                break
            else:
                print('退出购物！')
                break
        else:
            print('谢谢惠顾！')

@common.auth
def check_shop_cart():
    print('查看购物车'.center(50, '='))
    flag,msg = shop.check_shop_cart_interface(user_info['name'])
    if flag:
        print(msg)
    else:
        print(msg)
@common.auth
def logout():
    print('注销页面'.center(50, '='))
    msg = user.logout_interface(user_info['name'])
    print(msg)

func_dic={
    '1':register,
    '2':login,
    '3':check_balance,
    '4':withdraw,
    '5':transfer,
    '6':repay,
    '7':check_flow,
    '8':shopping,
    '9':check_shop_cart,
    '0':logout,
}
def run():
    while True:
        print('''
        1 注册
        2 登录
        3 查看余额
        4 提现
        5 转账
        6 还款
        7 查看流水
        8 购物
        9 查看购物车
        0 注销用户
        q 退出
        ''')
        choice = input('请输入操作>>:')
        if choice in func_dic:
            func_dic[choice]()
        elif choice == 'q' or 'Q':
            break
        else:
            print('输入有误!')
            continue


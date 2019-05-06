# 数据处理层
from conf import settings
import os,json
# 存数据
def save(user_dic):
    with open('%s/%s.json'%(settings.DB_PATH,user_dic['name']),'w',\
              encoding='utf-8')as f:
        f.write(json.dumps(user_dic))
        f.flush()
# 查取数据
def select(name):
    user_path = '%s/%s.json'%(settings.DB_PATH,name)
    if not os.path.exists(user_path):
        return
    with open(user_path,'r',encoding='utf-8')as f:
        user_dic = json.load(f)
        return user_dic

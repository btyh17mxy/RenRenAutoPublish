# -*-coding:utf-8-*-
'''
Created on 2013-5-21

@author: mush
'''
from ntype import NTYPES
import re
from renren import RenRen



# 匹配自己名字的正则@CityRun(601414776)
self_match_pattern = re.compile('@烟台高校信息发布平台(\(601742726\))?')

bot = RenRen()

# 从一条消息里取出要表白的对象和要说的话
# 内容格式因为“@CityRun(601414776) 我想跟牟俊秋(340352870)表白：我喜欢你很久了！”
def extractContent(message):
    content = self_match_pattern.sub('', message)
    #通过‘：’分割出表白对象和表白内容
    content_s = content.split(') ', 1)
    #name = content_s[0].split('跟', 1)[-1].split('(',1)[0]
    #uid = content_s[0].split('跟', 1)[-1].split('(',1)[-1].split(')',1)[0]
    content = content_s[-1]
    #print 'name: '+name+'  \tuid: '+uid+'\tcontent: '+content
    return content

# 将不同类型的消息统一成同一种形式
def getNotiData(data):
    ntype, content = int(data['type']), ''

    palyloads = {
        'id':int(data['notify_id']),
        'type':int(data['type']),
        'owner': int(data['owner']),
        'from': data['from'],
        'fromname':data['from_name'],
        'status':True
    }
    # 如果信息类型是‘悄悄话’

    if ntype == NTYPES['at_in_status']:
        palyloads['content']= data['doing_content']
        return palyloads
    """
    if ntype == NTYPES['reply_in_status_comment']:
        return palyloads
    if ntype == NTYPES['whisper']:
        print 'get whisper', data['msg_context']
        palyloads['content']= data['msg_context']
        return palyloads
        """
    palyloads


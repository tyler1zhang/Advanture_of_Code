import pandas as pd 
import numpy as np 
from datetime import datetime
#import time

def clean_by_sid(sid, df):
    #df[df['shopid'] == 57189823]
    #uid = 57189823
    dic_uid = {}
    sid_df = df[df['shopid'] == sid]

    for user in set(sid_df['userid']):
        dic_uid[user] = len(sid_df[sid_df['userid'] == user])

    #print(dic_uid)
    clean_dic_uid = dic_uid.copy()
    for key, value in dic_uid.items():
        if value < 3:
            del clean_dic_uid[key]
            
    #for key in clean_dic_uid.keys():
    c_sid_df = pd.DataFrame(columns = df.columns)
    for key in clean_dic_uid.keys():
        c_sid_df = c_sid_df.append(sid_df[sid_df['userid'] == key])
        
    return c_sid_df

def brush_uid00(sid, df):
    sid_df = clean_by_sid(sid, df)
    cheat_dic = {}
    for u in sid_df['userid']:
        cheat_dic[u] = len(sid_df[sid_df['userid'] == u])

    brush_uid_lst = []
    
    if len(cheat_dic) > 1:
        max_v = max(cheat_dic.values())
        for key, value in cheat_dic.items():
            if value == max_v:
                brush_uid_lst.append(key)
        brush_uid_lst.sort()
        uid = ''
        for i, k in enumerate(brush_uid_lst):
            if i == 0:
                uid += str(k)
            else:
                uid += ('&' +str(k))
    elif len(cheat_dic) == 1:
        uid = list(cheat_dic.values())[0]
    else:
        uid = 0
    return uid


raw_df = pd.read_csv('./order_brush_order.csv')

t_sec = []
for t in raw_df['event_time']:
    t_sec.append(int(time.mktime(datetime.strptime(t, "%Y-%m-%d %H:%M:%S").timetuple()))) 
    
# Add column seconds, which convert from datetime string.        
raw_df['seconds'] = t_sec

new_column = list(raw_df.columns)
new_column.remove('event_time')
df = raw_df[new_column]

# Check by shopid, count the order qty of this shopid in the whole data file, not consider the time yet.
dic_shopid_orderqty = {}
for shop in set(df['shopid']):
    dic_shopid_orderqty[shop] = len(df[df['shopid'] == shop])

# Create the dataframe of shopid and order_qty
# sorted by order qty
df_shopid_orderqty = pd.DataFrame({'shopid': list(dic_shopid_orderqty.keys()), 'order_qty': list(dic_shopid_orderqty.values())}).sort_values(by = ['order_qty'], ascending=0)

clean_sid_df = df_shopid_orderqty[df_shopid_orderqty['order_qty'] >2]
clean_sid_df

# clean_df = pd.DataFrame(columns = df.columns)
# for shop in clean_sid_df['shopid']:
#     clean_df = clean_df.append(clean_by_sid(shop, df))

# print(clean_df)

result_dic = {}
for shop in set(df['shopid']):
    if shop in set(clean_sid_df['shopid']):
        result_dic[shop] = brush_uid00(shop, df)
    else:
        result_dic[shop] = 0

result_df = pd.DataFrame({'shopid': list(result_dic.keys()), 'userid':list(result_dic.values())})
result_df.to_csv('result.csv')


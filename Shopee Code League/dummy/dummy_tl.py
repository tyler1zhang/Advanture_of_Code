import pandas as pd
import numpy as np 

dic = {'id': list(range(101)), 'new_number': list(range(2, 103))}
df = pd.DataFrame(data = dic)
print(df)

result = pd.to_csv

    uid = 57189823
    dic_uid = {}
    sid_df = df[df['shopid'] == uid]

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
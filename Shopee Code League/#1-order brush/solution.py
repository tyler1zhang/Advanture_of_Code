# -*- coding: utf-8 -*-
import csv
from datetime import datetime

def find_solution():
    shops_order={}
    with open('order_brush_order.csv') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        #orderid    shopid    userid    event_time
        for row in csv_reader:
            order_time=int(datetime.strptime(row['event_time'], "%Y-%m-%d  %H:%M:%S").timestamp())
            if row['shopid'] in shops_order:
                shops_order[row['shopid']].append((order_time, row['userid'],row['orderid']))
            else: shops_order[row['shopid']]=[(order_time, row['userid'], row['orderid']),]
    
    fieldnames=['shopid','userid']   
    csv_file= open('c1_2nd.csv', mode='w')
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)   
    writer.writeheader()

    for shopid, orders in shops_order.items():
        orders=sorted(orders, key=lambda tup: tup[0])
        suspicious_order=set()
            
        for j in range(1, len(orders)):
                if orders[j][0]-orders[0][0]<3600:
                    order_1h=orders[:j+1]            
                    user_count= len({order[1] for order in order_1h})
                    if len(order_1h)/user_count>=3:
                        update_suspicious_order(suspicious_order,order_1h)
                else: break
        for i in range(1, len(orders)):
            for j in range(i+1, len(orders)):
                if orders[j][0]-orders[i-1][0]>=3600 and orders[j-1][0]-orders[i][0]<3600:
                    order_1h=orders[i:j]            
                    user_count= len({order[1] for order in order_1h})
                    if len(order_1h)/user_count>=3:
                        update_suspicious_order(suspicious_order,order_1h)
                elif orders[j-1][0]-orders[i][0]>=3600: break
            if orders[-1][0]-orders[i][0]<3600:
                order_1h=orders[i:]            
                user_count= len({order[1] for order in order_1h})
                if len(order_1h)/user_count>=3:
                    update_suspicious_order(suspicious_order,order_1h)
            
        count_map={}
        for order in suspicious_order:
            if order[1] in count_map:
                count_map[order[1]]+=1
            else: count_map[order[1]]=1
        max_v, max_user=0, []
        for k, v in count_map.items():
            if v>max_v: 
                max_user=[int(k)]
                max_v=v
            elif v==max_v: max_user.append(int(k))
        if len(max_user)>1:
            
            row={'shopid':shopid, 'userid':'&'.join([str(user) for user in sorted(max_user)])}
        elif len(max_user)>0:
            row={'shopid':shopid, 'userid':max_user[0]}
        else:
            row={'shopid':shopid, 'userid':'0'}
        writer.writerow(row)
    csv_file.close()

def update_suspicious_order(suspicious_order, new_orders):
    for order in new_orders:
        suspicious_order.add(order)
        
find_solution()
                


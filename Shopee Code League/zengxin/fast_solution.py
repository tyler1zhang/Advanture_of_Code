# -*- coding: utf-8 -*-
import csv
import time

#### to write data to csv file####
def write_csv(file, fieldnames, data:list):
    with open(file, mode='w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for row in data:
            writer.writerow(row)

### convert time to epoch time ###
def convert_to_epoch(str_time):
    pattern = '%Y-%m-%d %H:%M:%S'
    epoch = int(time.mktime(time.strptime(str_time, pattern)))
    return epoch

def get_time(f):
    def cal_time():
        start_time = time.time()
        f()
        print(time.time() - start_time, "seconds")
    return cal_time

FINAL_DATA = []

# Global data
with open("order_brush_order.csv", newline="") as f:
    csv_reader = csv.reader(f, delimiter=',')
    ITEM_LIST = list(csv_reader)[1:]
    # print(ITEM_LIST[:2])
    print("starting", len(ITEM_LIST), "records" )
f.close()

@get_time
def main():
    all_records = {}
    for transaction in ITEM_LIST:
        shopid, userid = transaction[1], transaction[2]
        if shopid not in all_records:
            all_records[shopid]={"counter":1, "buyers":{userid:[1,transaction[3]]}}
        else:
            all_records[shopid]["counter"]+=1
            if userid in all_records[shopid]["buyers"]:
                all_records[shopid]["buyers"][userid][0]+=1
                all_records[shopid]["buyers"][userid].append(transaction[3])
            else:
                all_records[shopid]["buyers"][userid]=[1,transaction[3]]
    # print(all_records['10287'])
    for shopid, records in all_records.items():
        if records["counter"] < 3:
            FINAL_DATA.append({"shopid":shopid,"userid":0})
        else:
            brush_users= {}
            for userid, [count, *transac_times] in records["buyers"].items():
                # print(count)
                # print(transac_times)
                valid = {} # valid = {"brush_count":100}
                if count < 3:
                    valid["brush_count"]=0
                    # print("no brushing", userid)
                elif count > 2:
                    epoch_transac_times = [convert_to_epoch(i) for i in transac_times ]
                    epoch_transac_times.sort()
                    # capture any consecutive trans in a hour
                    valid_transacs = []
                    for index, time in enumerate(epoch_transac_times[2:]):
                        if (time - epoch_transac_times[index]) < 3601:
                            valid_transacs.extend([epoch_transac_times[index],epoch_transac_times[index+1], epoch_transac_times[index+2]])
                            print(epoch_transac_times[index],epoch_transac_times[index+1], epoch_transac_times[index+2])
                    # all transaction happen in this period counts, so those other users trans in thie periods also counts
                    # need to all user to valid and check in this period if other valid users
                    valid["brush_count"]=len(set(valid_transacs))
                    print(len(set(valid_transacs)))
                if valid["brush_count"] != 0:
                    brush_users[userid] = valid["brush_count"]
            if brush_users:
                max_count = max(brush_users.values())
                print(max_count)
                userids = []
                for userid, brush_counter in brush_users.items():
                    if brush_counter == max_count:
                        userids.append(userid)
                userids.sort()
                brushers = "&".join(userids)
                FINAL_DATA.append({"shopid":shopid,"userid":brushers})
            else:
                FINAL_DATA.append({"shopid":shopid,"userid":0})

    print("finish",len(all_records), "items")

main()

def write_result():
    file = 'result_gtzz4.csv'
    fieldnames = ['shopid', 'userid'] 
    write_csv(file, fieldnames, FINAL_DATA)

write_result()
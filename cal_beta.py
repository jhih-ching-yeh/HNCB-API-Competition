import csv 
import os
csv_columns = ['ID', 'result']

a=[[0]*3 for i in range(2000)]
a[0][0] = 'ID'
a[0][1] = 'result'
a[0][2] = 'n'

s = 0
for info in os.listdir(r'data'):
    domain = os.path.abspath(r'data')
    x = info
    info = os.path.join(domain,info)
        #print(info)
    if info != '/Users/yuchanghuang/Documents/JOBS/SUNNY/data/.DS_Store':
        with open(info, newline='') as csvFile:


            rows = csv.DictReader(csvFile)
            uper_count = 0.0
            count = 0.0
            #n_count = 0
            for row in rows:
                if row['buy_category'] == '買':
                    #print('!!')
                    #print(info)
                    #print(row['stock_code']+'AAAAA')
                    #print(rows[0])
                    #count = count + float(row['num_of_shares'])
                    #print (count)
                    with open('beta_test_1.csv', newline='') as stock:
                        stocks_row = csv.DictReader(stock)
                        for stock_stuff in stocks_row:
                            #print (row['num_of_shares'], row['trans_category'])
                            #print(row['stock_code'])
                            #print(info)
                            if stock_stuff['T'] == row['stock_code']:
                                #print(stock_stuff['T'], row['stock_code'])
                                #print(info)
                                #n_count += 1
                                uper_count += float(row['num_of_shares']) * float(stock_stuff['Beta'])
                                count  = count + float(row['num_of_shares'])
            #print(info)

            a[s][0] = x
            if count == 0:

                a[s][1] = 0
            else:
                a[s][1] = uper_count/count
                #print(count)
            a[s][2] = count
            print (a[s][0], a[s][1], a[s][2])
    s = s + 1
with open('output2.csv', 'w', newline='') as output:
  # 建立 CSV 檔寫入器
  writer = csv.writer(output)

  writer.writerow(['ID', 'result', 'n'])
  for i in range (s):
        writer.writerow([a[i][0], a[i][1], a[i][2]])
#print (a)
                

    
